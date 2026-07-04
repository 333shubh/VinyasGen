from typing import Any


def layout_to_dxf(layout: dict[str, Any]) -> str:
    lines = ["0", "SECTION", "2", "ENTITIES"]
    for feature in layout.get("geojson", {}).get("features", []):
        geometry = feature.get("geometry", {})
        if geometry.get("type") != "Polygon":
            continue
        coords = geometry.get("coordinates", [[]])[0]
        for start, end in zip(coords, coords[1:]):
            lines.extend(
                [
                    "0",
                    "LINE",
                    "8",
                    feature.get("properties", {}).get("zone", "layout"),
                    "10",
                    str(start[0]),
                    "20",
                    str(start[1]),
                    "11",
                    str(end[0]),
                    "21",
                    str(end[1]),
                ]
            )
    lines.extend(["0", "ENDSEC", "0", "EOF"])
    return "\n".join(lines)
