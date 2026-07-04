from __future__ import annotations

from typing import Any

from shapely.geometry import shape

from engine.geo_utils import to_utm


def compute_impact_metrics(
    site_utm,
    zones_utm: dict[str, Any],
    parking_metrics: dict[str, Any],
    layout_geojson: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if layout_geojson:
        return compute_rendered_impact_metrics(site_utm, layout_geojson, parking_metrics)

    total_area = max(site_utm.area, 0.01)
    green_area = sum(zones_utm[key].area for key in ("green", "open_space") if key in zones_utm)
    building_area = zones_utm.get("building").area if "building" in zones_utm else 0.0
    footpath_area = zones_utm.get("footpath").area if "footpath" in zones_utm else 0.0
    parking_area = zones_utm.get("parking").area if "parking" in zones_utm else 0.0
    drain_area = zones_utm.get("drain").area if "drain" in zones_utm else 0.0
    parking_spaces = int(parking_metrics.get("parking_spaces", 0))
    cost_lakh = (
        green_area * 0.007
        + footpath_area * 0.006
        + parking_area * 0.004
        + drain_area * 0.011
        + parking_spaces * 0.0025
    )
    metrics = {
        "site_area_sqm": round(total_area, 2),
        "green_area_sqm": round(green_area, 2),
        "ground_coverage_area_sqm": round(building_area, 2),
        "floor_area_sqm": round(building_area, 2),
        "far": round(building_area / total_area, 3),
        "green_cover_pct": round((green_area / total_area) * 100, 1),
        "built_cover_pct": round((building_area / total_area) * 100, 1),
        "parking_spaces": parking_spaces,
        "parking_efficiency_pct": parking_metrics.get("parking_efficiency_pct", 0),
        "tree_count": max(0, int(green_area // 28)),
        "walkable_path_m": round(footpath_area / 1.5, 1) if footpath_area else 0,
        "walking_priority": round((footpath_area / total_area) * 100, 1),
        "thermal_score_delta_c": round(min(8.0, green_area / total_area * 12), 1),
        "drainage_capacity_mm_hr": round(25 + (drain_area / total_area) * 900, 1),
        "estimated_cost_lakh": round(cost_lakh, 2),
    }
    metrics["livability_score"] = compute_livability_score(metrics)
    return metrics


def compute_rendered_impact_metrics(
    site_utm,
    layout_geojson: dict[str, Any],
    parking_metrics: dict[str, Any] | None = None,
) -> dict[str, Any]:
    total_area = max(site_utm.area, 0.01)
    areas = {
        "green": 0.0,
        "open_space": 0.0,
        "building": 0.0,
        "footpath": 0.0,
        "parking": 0.0,
        "drain": 0.0,
    }
    parking_spaces = 0
    for feature in layout_geojson.get("features", []):
        geometry = feature.get("geometry", {})
        properties = feature.get("properties", {})
        zone_type = properties.get("zone_type") or properties.get("zone")
        if zone_type == "parking_stall":
            parking_spaces += 1
            continue
        if geometry.get("type") != "Polygon" or zone_type not in areas:
            continue
        areas[zone_type] += to_utm(shape(geometry)).area

    green_area = areas["green"] + areas["open_space"]
    building_area = areas["building"]
    footpath_area = areas["footpath"]
    parking_area = areas["parking"]
    drain_area = areas["drain"]
    parking_efficiency = 0
    if parking_metrics and "parking_efficiency_pct" in parking_metrics:
        parking_efficiency = parking_metrics["parking_efficiency_pct"]
    elif parking_area:
        parking_efficiency = round((parking_spaces * 2.5 / parking_area) * 100, 1)

    cost_lakh = (
        green_area * 0.007
        + footpath_area * 0.006
        + parking_area * 0.004
        + drain_area * 0.011
        + parking_spaces * 0.0025
    )
    metrics = {
        "site_area_sqm": round(total_area, 2),
        "green_area_sqm": round(green_area, 2),
        "ground_coverage_area_sqm": round(building_area, 2),
        "floor_area_sqm": round(building_area, 2),
        "far": round(building_area / total_area, 3),
        "green_cover_pct": round((green_area / total_area) * 100, 1),
        "built_cover_pct": round((building_area / total_area) * 100, 1),
        "parking_spaces": parking_spaces,
        "parking_efficiency_pct": parking_efficiency,
        "tree_count": max(0, int(green_area // 28)),
        "walkable_path_m": round(footpath_area / 1.5, 1) if footpath_area else 0,
        "walking_priority": round((footpath_area / total_area) * 100, 1),
        "thermal_score_delta_c": round(min(8.0, green_area / total_area * 12), 1),
        "drainage_capacity_mm_hr": round(25 + (drain_area / total_area) * 900, 1),
        "estimated_cost_lakh": round(cost_lakh, 2),
    }
    metrics["livability_score"] = compute_livability_score(metrics)
    return metrics


def compute_livability_score(metrics: dict[str, Any]) -> int:
    green = min(float(metrics.get("green_cover_pct", 0)), 40) / 40
    walking = min(float(metrics.get("walking_priority", 0)), 30) / 30
    parking = min(float(metrics.get("parking_spaces", 0)), 30) / 30
    thermal = min(float(metrics.get("thermal_score_delta_c", 0)), 8) / 8
    score = (green * 35) + (walking * 25) + (parking * 20) + (thermal * 20)
    return round(score)
