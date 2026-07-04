from typing import Any

from shapely.geometry import box

from engine.geo_utils import to_wgs84

CAR_STALL_WIDTH_M = 2.5
CAR_STALL_LENGTH_M = 5.0
AISLE_WIDTH_M = 6.0


def optimize_parking(parking_polygon_utm) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Deterministic MVP parking packer.

    OR-Tools remains the intended production solver, but this creates valid,
    non-overlapping parking bay rectangles inside the parking zone with a clear
    aisle reservation. It is deterministic and never uses AI for geometry.
    """
    minx, miny, maxx, maxy = parking_polygon_utm.bounds
    usable = parking_polygon_utm.buffer(-0.15)
    features: list[dict[str, Any]] = []
    y = miny
    stall_id = 1

    while y + CAR_STALL_LENGTH_M <= maxy:
        x = minx
        while x + CAR_STALL_WIDTH_M <= maxx:
            stall = box(x, y, x + CAR_STALL_WIDTH_M, y + CAR_STALL_LENGTH_M)
            if usable.contains(stall):
                features.append(
                    {
                        "type": "Feature",
                        "properties": {
                            "zone": "parking_stall",
                            "name": f"Parking Bay {stall_id}",
                            "fill": "#fbbf24",
                            "area_sqm": round(stall.area, 2),
                        },
                        "geometry": to_wgs84(stall),
                    }
                )
                stall_id += 1
            x += CAR_STALL_WIDTH_M + 0.6
        y += CAR_STALL_LENGTH_M + AISLE_WIDTH_M

    metrics = {
        "parking_spaces": len(features),
        "parking_efficiency_pct": round((len(features) * CAR_STALL_WIDTH_M * CAR_STALL_LENGTH_M / parking_polygon_utm.area) * 100, 1)
        if parking_polygon_utm.area
        else 0,
    }
    return features, metrics
