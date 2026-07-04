from __future__ import annotations

from typing import Any

from shapely.geometry import LineString, Point, shape
from shapely.ops import unary_union

from engine.geo_utils import to_utm, to_wgs84


def _feature_polygons(layout_geojson: dict[str, Any], zone_type: str):
    polygons = []
    for feature in layout_geojson.get("features", []):
        props = feature.get("properties", {})
        if props.get("zone_type") == zone_type or props.get("zone") == zone_type:
            polygons.append(to_utm(shape(feature["geometry"])))
    return polygons


def check_emergency_access(layout_geojson: dict[str, Any], constraints: dict[str, Any]) -> dict[str, Any]:
    fire = constraints.get("fire_safety", {})
    min_width = float(fire.get("min_clear_access_width_m", 4.5))
    min_turning_radius = float(fire.get("min_turning_radius_m", 9.0))
    max_dead_end = float(fire.get("max_dead_end_length_m", 30.0))
    vehicle_polygons = _feature_polygons(layout_geojson, "vehicle")
    violations: list[dict[str, Any]] = []

    if not vehicle_polygons:
        return {
            "overall_status": "FAIL",
            "violations": [{"type": "missing_clear_path", "location": None, "detail": "No vehicle carriageway zone exists."}],
            "clear_path_geojson": {"type": "FeatureCollection", "features": []},
        }

    vehicle = unary_union(vehicle_polygons)
    minx, miny, maxx, maxy = vehicle.bounds
    clear_width = min(maxx - minx, maxy - miny)
    length = max(maxx - minx, maxy - miny)
    centroid = vehicle.centroid

    if clear_width < min_width:
        violations.append(
            {
                "type": "min_clear_width",
                "location": list(to_wgs84(Point(centroid.x, centroid.y))["coordinates"]),
                "detail": f"Clear path width is {clear_width:.2f}m; required minimum is {min_width:.2f}m.",
            }
        )
    if clear_width / 2 < min_turning_radius and length > min_turning_radius * 2:
        violations.append(
            {
                "type": "turning_radius",
                "location": list(to_wgs84(Point(centroid.x, centroid.y))["coordinates"]),
                "detail": f"Available turning radius is approximately {clear_width / 2:.2f}m; required is {min_turning_radius:.2f}m.",
            }
        )
    if length > max_dead_end and clear_width < min_width * 1.25:
        violations.append(
            {
                "type": "dead_end_length",
                "location": list(to_wgs84(Point(centroid.x, centroid.y))["coordinates"]),
                "detail": f"Potential dead-end length is {length:.2f}m; maximum is {max_dead_end:.2f}m.",
            }
        )

    if (maxx - minx) >= (maxy - miny):
        path = LineString([(minx, (miny + maxy) / 2), (maxx, (miny + maxy) / 2)])
    else:
        path = LineString([((minx + maxx) / 2, miny), ((minx + maxx) / 2, maxy)])

    status = "FAIL" if violations else "PASS"
    return {
        "overall_status": status,
        "violations": violations,
        "clear_path_geojson": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {"status": status, "clear_width_m": round(clear_width, 2)},
                    "geometry": to_wgs84(path),
                }
            ],
        },
    }
