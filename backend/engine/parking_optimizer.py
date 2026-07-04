from __future__ import annotations

from typing import Any

from shapely.geometry import box

from engine.geo_utils import to_wgs84

TWO_WHEELER_WIDTH_M = 1.0
TWO_WHEELER_LENGTH_M = 2.5
CAR_WIDTH_M = 2.5
CAR_LENGTH_M = 5.0
TWO_WHEELER_AISLE_M = 3.0


def optimize_parking(parking_polygon_utm) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    usable = parking_polygon_utm.buffer(-0.1)
    minx, miny, maxx, maxy = usable.bounds
    features: list[dict[str, Any]] = []
    stall_id = 1
    row_height = TWO_WHEELER_LENGTH_M + TWO_WHEELER_AISLE_M
    y = miny
    while y + TWO_WHEELER_LENGTH_M <= maxy:
        x = minx
        while x + TWO_WHEELER_WIDTH_M <= maxx:
            stall = box(x, y, x + TWO_WHEELER_WIDTH_M, y + TWO_WHEELER_LENGTH_M)
            if usable.contains(stall):
                features.append(_stall_feature(stall, stall_id, "two_wheeler"))
                stall_id += 1
            x += TWO_WHEELER_WIDTH_M + 0.25
        y += row_height

    used_area = len(features) * TWO_WHEELER_WIDTH_M * TWO_WHEELER_LENGTH_M
    metrics = {
        "parking_spaces": len(features),
        "two_wheeler_spaces": len(features),
        "car_spaces": 0,
        "parking_efficiency_pct": round((used_area / parking_polygon_utm.area) * 100, 1) if parking_polygon_utm.area else 0,
    }
    return features, metrics


def _stall_feature(stall, stall_id: int, vehicle_type: str) -> dict[str, Any]:
    return {
        "type": "Feature",
        "properties": {
            "zone_type": "parking_stall",
            "zone": "parking_stall",
            "vehicle_type": vehicle_type,
            "name": f"Two-Wheeler Bay {stall_id}",
            "area_sqm": round(stall.area, 2),
            "fill": "#7BA7D0",
            "stroke": "#2E6DA4",
        },
        "geometry": to_wgs84(stall),
    }
