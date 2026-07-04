from dataclasses import dataclass
from typing import Any

from shapely.geometry import box

from engine.compliance_checker import check_layout
from engine.geo_utils import to_utm43n, to_wgs84
from engine.green_space import place_trees
from engine.parking_optimizer import optimize_parking
from engine.scoring import compute_livability_score


@dataclass(frozen=True)
class ObjectiveProfile:
    key: str
    label: str
    density_shift: float
    green_shift: float
    pedestrian_shift: float


PROFILES = [
    ObjectiveProfile("balanced", "Balanced Community Plan", 0.0, 0.0, 0.0),
    ObjectiveProfile("max_green", "More Green Cover", -0.12, 0.18, 0.08),
    ObjectiveProfile("max_parking", "More Organized Parking", 0.08, -0.08, -0.05),
    ObjectiveProfile("walkable", "Safer Walking Route", -0.08, 0.06, 0.2),
]

ZONE_STYLES = {
    "built": {"label": "Community Use", "color": "#5271ff"},
    "parking": {"label": "Parking", "color": "#f59e0b"},
    "green": {"label": "Green Cover", "color": "#2f855a"},
    "path": {"label": "Walking Path", "color": "#64748b"},
}


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _largest_polygon(geom):
    if geom.geom_type == "Polygon":
        return geom
    if geom.geom_type == "MultiPolygon":
        return max(geom.geoms, key=lambda item: item.area)
    return geom


def _split_into_zones(plot_utm, weights: dict[str, float]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    minx, miny, maxx, maxy = plot_utm.bounds
    cursor = minx
    width = maxx - minx
    zones = []
    utm_zones = {}

    for index, (zone_name, weight) in enumerate(weights.items()):
        next_cursor = maxx if index == len(weights) - 1 else cursor + width * weight
        strip = box(cursor, miny, next_cursor, maxy)
        clipped = _largest_polygon(plot_utm.intersection(strip))
        cursor = next_cursor
        if clipped.is_empty:
            continue
        utm_zones[zone_name] = clipped
        style = ZONE_STYLES[zone_name]
        zones.append(
            {
                "type": "Feature",
                "properties": {
                    "zone": zone_name,
                    "name": style["label"],
                    "fill": style["color"],
                    "area_sqm": round(clipped.area, 2),
                },
                "geometry": to_wgs84(clipped),
            }
        )

    return zones, utm_zones


def _weights(slider_values: dict[str, float], profile: ObjectiveProfile, site_type: str) -> dict[str, float]:
    density = _clamp(float(slider_values.get("density_level", 0.45)) + profile.density_shift, 0.05, 0.75)
    green = _clamp(float(slider_values.get("greenery_pct", 0.25)) + profile.green_shift, 0.08, 0.75)
    pedestrian = _clamp(
        float(slider_values.get("pedestrian_priority", 0.4)) + profile.pedestrian_shift,
        0.05,
        0.8,
    )

    if site_type == "street_regeneration":
        built = density * 0.15
        path = 0.22 + pedestrian * 0.28
        parking = 0.42 - green * 0.16
    elif site_type == "public_space":
        built = density * 0.18
        path = 0.18 + pedestrian * 0.2
        parking = 0.16
    else:
        built = 0.16 + density * 0.36
        path = 0.12 + pedestrian * 0.16
        parking = 0.22

    raw = {
        "built": max(0.04, built),
        "parking": max(0.04, parking),
        "green": max(0.08, green),
        "path": max(0.04, path),
    }
    total = sum(raw.values())
    return {key: value / total for key, value in raw.items()}


def generate_layout_options(
    plot_geojson: dict[str, Any],
    slider_values: dict[str, float],
    regulations: dict[str, Any],
    site_type: str,
) -> list[dict[str, Any]]:
    plot_utm = _largest_polygon(to_utm43n(plot_geojson))
    if plot_utm.area <= 0:
        raise ValueError("Drawn area is not valid. Please redraw the plot or lane.")

    options = []
    for profile in PROFILES:
        weights = _weights(slider_values, profile, site_type)
        features, utm_zones = _split_into_zones(plot_utm, weights)
        parking_features, parking_metrics = optimize_parking(utm_zones["parking"]) if "parking" in utm_zones else ([], {})
        tree_features, tree_metrics = place_trees(utm_zones["green"]) if "green" in utm_zones else ([], {})
        features.extend(parking_features)
        features.extend(tree_features)
        zone_areas = {
            feature["properties"]["zone"]: feature["properties"]["area_sqm"]
            for feature in features
            if "area_sqm" in feature["properties"]
        }
        total_area = round(plot_utm.area, 2)
        green_area = zone_areas.get("green", 0)
        built_area = zone_areas.get("built", 0)
        parking_area = zone_areas.get("parking", 0)
        metrics = {
            "site_area_sqm": total_area,
            "green_cover_pct": round((green_area / total_area) * 100, 1),
            "built_cover_pct": round((built_area / total_area) * 100, 1),
            "parking_spaces": parking_metrics.get("parking_spaces", int(parking_area // 23)),
            "parking_efficiency_pct": parking_metrics.get("parking_efficiency_pct", 0),
            "tree_count": tree_metrics.get("tree_count", 0),
            "walking_priority": round(weights.get("path", 0) * 100, 1),
            "estimated_cost_lakh": round((green_area * 0.018) + (parking_area * 0.012) + (built_area * 0.025), 2),
        }
        metrics["livability_score"] = compute_livability_score(metrics)
        compliance = check_layout(metrics, regulations)

        options.append(
            {
                "layout_id": f"layout_{profile.key}",
                "objective_profile": profile.label,
                "geojson": {
                    "type": "FeatureCollection",
                    "features": features,
                },
                "metrics": metrics,
                "compliance_summary": compliance,
            }
        )

    return options
