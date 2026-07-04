from __future__ import annotations

from string import ascii_uppercase
from typing import Any

from shapely.geometry import shape

from engine.geo_utils import to_utm, to_wgs84


def calculate_encroachments(official_geojson: dict[str, Any], actual_geojson: dict[str, Any]) -> dict[str, Any]:
    official = to_utm(shape(official_geojson.get("geometry", official_geojson)))
    actual = to_utm(shape(actual_geojson.get("geometry", actual_geojson)))
    diff = official.difference(actual)
    polygons = []
    if diff.is_empty:
        parts = []
    elif diff.geom_type == "Polygon":
        parts = [diff]
    else:
        parts = [geom for geom in diff.geoms if geom.geom_type == "Polygon" and geom.area > 0.01]

    for index, polygon in enumerate(parts):
        label = f"Structure {ascii_uppercase[index] if index < len(ascii_uppercase) else index + 1}"
        depth = _estimate_depth_m(polygon)
        polygons.append(
            {
                "type": "Feature",
                "properties": {
                    "anon_label": label,
                    "depth_m": round(depth, 2),
                    "area_sqm": round(polygon.area, 2),
                    "detection_mode": "manual",
                    "confidence": "indicative",
                    "verified": False,
                    "zone_type": "encroachment",
                    "fill": "#E74C3C",
                    "stroke": "#C0392B",
                },
                "geometry": to_wgs84(polygon),
            }
        )

    return {
        "encroachments": {"type": "FeatureCollection", "features": polygons},
        "summary": {
            "count": len(polygons),
            "total_area_sqm": round(sum(item["properties"]["area_sqm"] for item in polygons), 2),
            "max_depth_m": max((item["properties"]["depth_m"] for item in polygons), default=0),
        },
    }


def _estimate_depth_m(polygon) -> float:
    minx, miny, maxx, maxy = polygon.bounds
    longest_side = max(maxx - minx, maxy - miny, 0.01)
    return polygon.area / longest_side
