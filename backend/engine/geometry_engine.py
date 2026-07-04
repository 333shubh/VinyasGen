from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from shapely.geometry import LineString, Polygon, box, shape
from shapely.ops import transform
from shapely.validation import make_valid

from engine.access_checker import check_emergency_access
from engine.compliance_checker import check_layout
from engine.geo_utils import _to_utm43n, to_wgs84
from engine.parking_optimizer import optimize_parking
from engine.scoring import compute_impact_metrics


class SetbackExceedsPlotError(ValueError):
    pass


ZONE_STYLES = {
    "vehicle": {"fill_color": "#D9D9D9", "stroke_color": "#999999", "label": "Vehicle Carriageway"},
    "parking": {"fill_color": "#A8C8E8", "stroke_color": "#4A90D9", "label": "Two-Wheeler Parking"},
    "footpath": {"fill_color": "#F5E6C8", "stroke_color": "#C4A46B", "label": "Footpath"},
    "drain": {"fill_color": "#85C1E9", "stroke_color": "#2E86AB", "label": "Drain Channel"},
    "green": {"fill_color": "#A8D5A2", "stroke_color": "#4F9D69", "label": "Green / Planter Strip"},
    "building": {"fill_color": "#C7B7A3", "stroke_color": "#7A6652", "label": "Buildable Area"},
    "open_space": {"fill_color": "#A8D5A2", "stroke_color": "#4F9D69", "label": "Open / Green Area"},
}

OBJECTIVE_PROFILES = {
    "max_parking": {"vehicle": 0.45, "parking": 0.30, "footpath": 0.12, "drain": 0.05, "green": 0.08},
    "max_green": {"vehicle": 0.40, "parking": 0.10, "footpath": 0.18, "drain": 0.07, "green": 0.25},
    "pedestrian": {"vehicle": 0.35, "parking": 0.10, "footpath": 0.30, "drain": 0.07, "green": 0.18},
    "fire_safe": {"vehicle": 0.55, "parking": 0.20, "footpath": 0.12, "drain": 0.05, "green": 0.08},
    "balanced": {"vehicle": 0.42, "parking": 0.20, "footpath": 0.18, "drain": 0.06, "green": 0.14},
}

OBJECTIVE_LABELS = {
    "max_parking": "Maximum Parking",
    "max_green": "Maximum Green Cover",
    "pedestrian": "Pedestrian First",
    "fire_safe": "Fire Safety Optimized",
    "balanced": "Balanced Community",
}


@dataclass(frozen=True)
class LayoutContext:
    total_width_m: float | None = None


def normalize_boundary(geojson_geometry: dict[str, Any]) -> Polygon:
    geometry = geojson_geometry.get("geometry", geojson_geometry)
    geom = make_valid(shape(geometry))
    if geom.geom_type == "MultiPolygon":
        geom = max(geom.geoms, key=lambda item: item.area)
    if geom.geom_type != "Polygon":
        raise ValueError("Boundary must be a Polygon or Polygon Feature.")
    if geom.is_empty or not geom.is_valid or geom.area <= 0:
        raise ValueError("Boundary geometry is invalid after repair.")
    return geom


def to_utm(shapely_geom):
    return transform(_to_utm43n, shapely_geom)


def apply_setback(plot_utm: Polygon, setback_m: float) -> Polygon:
    buildable = make_valid(plot_utm.buffer(-setback_m, join_style=2))
    if buildable.is_empty:
        raise SetbackExceedsPlotError("Required setbacks exceed the drawn boundary.")
    if buildable.geom_type == "MultiPolygon":
        return max(buildable.geoms, key=lambda item: item.area)
    if buildable.geom_type != "Polygon":
        raise SetbackExceedsPlotError("Setback operation did not produce a usable polygon.")
    return buildable


def _largest_polygon(geom) -> Polygon:
    if geom.geom_type == "Polygon":
        return geom
    if geom.geom_type == "MultiPolygon":
        return max(geom.geoms, key=lambda item: item.area)
    raise ValueError("Expected polygonal geometry.")


def _split_corridor_by_width(corridor_utm: Polygon, allocation: dict[str, float]) -> dict[str, Polygon]:
    minx, miny, maxx, maxy = corridor_utm.bounds
    width = maxx - minx
    cursor = minx
    zones: dict[str, Polygon] = {}
    items = list(allocation.items())
    for index, (zone_name, share) in enumerate(items):
        next_cursor = maxx if index == len(items) - 1 else cursor + (width * share)
        clipped = corridor_utm.intersection(box(cursor, miny, next_cursor, maxy))
        cursor = next_cursor
        if not clipped.is_empty:
            zones[zone_name] = _largest_polygon(clipped)
    return zones


def generate_cross_section_zones(
    centerline_utm: LineString,
    total_width_m: float,
    allocation: dict[str, float],
) -> dict[str, Polygon]:
    corridor = centerline_utm.buffer(total_width_m / 2, cap_style="flat", join_style=2)
    return _split_corridor_by_width(corridor, allocation)


def _slider_adjusted_allocation(base: dict[str, float], slider_values: dict[str, float]) -> dict[str, float]:
    adjusted = dict(base)
    adjusted["parking"] *= 0.75 + float(slider_values.get("density_level", 0.45))
    adjusted["green"] *= 0.75 + float(slider_values.get("greenery_pct", 0.25))
    adjusted["footpath"] *= 0.75 + float(slider_values.get("pedestrian_priority", 0.4))
    total = sum(adjusted.values())
    return {key: value / total for key, value in adjusted.items()}


def _site_width(plot_utm: Polygon, context: LayoutContext) -> float:
    if context.total_width_m:
        return context.total_width_m
    minx, miny, maxx, maxy = plot_utm.bounds
    return min(maxx - minx, maxy - miny)


def _corridor_centerline(plot_utm: Polygon) -> LineString:
    minx, miny, maxx, maxy = plot_utm.bounds
    if (maxx - minx) >= (maxy - miny):
        y = (miny + maxy) / 2
        return LineString([(minx, y), (maxx, y)])
    x = (minx + maxx) / 2
    return LineString([(x, miny), (x, maxy)])


def _plot_zones(plot_utm: Polygon, constraints: dict[str, Any], allocation: dict[str, float]) -> dict[str, Polygon]:
    plot_allocation = {
        "building": allocation["vehicle"],
        "parking": allocation["parking"],
        "footpath": allocation["footpath"],
        "drain": allocation["drain"],
        "green": allocation["green"],
    }
    return _split_corridor_by_width(plot_utm, plot_allocation)


def zones_to_geojson(zones_utm: dict[str, Polygon], metadata: dict[str, Any]) -> dict[str, Any]:
    features = []
    for zone_name, geom in zones_utm.items():
        style = ZONE_STYLES.get(zone_name, ZONE_STYLES["open_space"])
        features.append(
            {
                "type": "Feature",
                "properties": {
                    "zone_type": zone_name,
                    "zone": zone_name,
                    "name": style["label"],
                    "area_sqm": round(geom.area, 2),
                    "compliance_status": metadata.get("compliance_status", "unchecked"),
                    "compliance_detail": metadata.get("compliance_detail", ""),
                    "style": {
                        "fill_color": style["fill_color"],
                        "stroke_color": style["stroke_color"],
                        "opacity": 0.46,
                    },
                    "fill": style["fill_color"],
                    "stroke": style["stroke_color"],
                },
                "geometry": to_wgs84(geom),
            }
        )
    return {"type": "FeatureCollection", "features": features}


def generate_all_options(
    road_geometry: dict[str, Any],
    total_width_m: float | None,
    constraints: dict[str, Any],
    slider_values: dict[str, float] | None = None,
    site_type: str = "gali",
    regulations: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    boundary_utm = to_utm(normalize_boundary(road_geometry))
    context = LayoutContext(total_width_m=total_width_m)
    width_m = _site_width(boundary_utm, context)
    centerline = _corridor_centerline(boundary_utm)
    options = []
    for profile_key, base_allocation in OBJECTIVE_PROFILES.items():
        allocation = _slider_adjusted_allocation(base_allocation, slider_values or {})
        if site_type in {"road", "gali", "street_regeneration"}:
            raw_zones = generate_cross_section_zones(centerline, width_m, allocation)
            zones = {
                key: _largest_polygon(value.intersection(boundary_utm))
                for key, value in raw_zones.items()
                if not value.intersection(boundary_utm).is_empty
            }
        else:
            zones = _plot_zones(boundary_utm, constraints, allocation)
        parking_features, parking_metrics = optimize_parking(zones["parking"]) if "parking" in zones else ([], {})
        geojson = zones_to_geojson(zones, {"compliance_status": "unchecked"})
        geojson["features"].extend(parking_features)
        metrics = compute_impact_metrics(boundary_utm, zones, parking_metrics, geojson)
        compliance = check_layout(metrics, regulations or {"constraints": constraints}, geojson)
        access = check_emergency_access(geojson, constraints)
        metrics["emergency_access"] = access["overall_status"]
        options.append(
            {
                "layout_id": f"layout_{profile_key}",
                "objective_profile": OBJECTIVE_LABELS[profile_key],
                "geojson": geojson,
                "metrics": metrics,
                "compliance_summary": compliance,
                "emergency_access": access,
                "slider_values": slider_values or {},
            }
        )
    return options


def generate_layout_options(
    plot_geojson: dict[str, Any],
    slider_values: dict[str, float],
    regulations: dict[str, Any],
    site_type: str,
    total_width_m: float | None = None,
) -> list[dict[str, Any]]:
    return generate_all_options(
        plot_geojson,
        total_width_m,
        regulations.get("constraints", {}),
        slider_values,
        site_type,
        regulations,
    )
