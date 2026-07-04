from typing import Any

from shapely.geometry import Point

from engine.geo_utils import to_wgs84


def place_trees(green_polygon_utm, spacing_m: float = 7.0) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    minx, miny, maxx, maxy = green_polygon_utm.bounds
    features: list[dict[str, Any]] = []
    y = miny + spacing_m / 2
    tree_id = 1

    while y <= maxy:
        x = minx + spacing_m / 2
        while x <= maxx:
            point = Point(x, y)
            if green_polygon_utm.contains(point):
                features.append(
                    {
                        "type": "Feature",
                        "properties": {
                            "zone": "tree",
                            "name": f"Tree {tree_id}",
                            "fill": "#166534",
                        },
                        "geometry": to_wgs84(point),
                    }
                )
                tree_id += 1
            x += spacing_m
        y += spacing_m

    return features, {"tree_count": len(features)}
