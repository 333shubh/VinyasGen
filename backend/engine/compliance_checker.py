from __future__ import annotations

from typing import Any

LEGAL_DISCLAIMER = (
    "VinyasGen is a decision-support and visualization tool. All outputs - layouts, "
    "compliance results, cost estimates, and encroachment flags - are indicative only, "
    "based on digitized regulatory data, and do not constitute statutory approval, "
    "legal measurement, or enforcement action. All proposals must be verified with the "
    "relevant municipal authority before implementation. Encroachment flags are "
    "potential indicators requiring field verification - they do not constitute legal evidence."
)


def _citation(regulations: dict[str, Any], section: str, value: Any) -> str:
    document = regulations.get("source_document", "Pending source review")
    return f"{document}; {section}; value={value}"


def check_layout(
    metrics: dict[str, Any],
    regulations: dict[str, Any],
    layout_geojson: dict[str, Any] | None = None,
) -> dict[str, Any]:
    constraints = regulations.get("constraints", {})
    checks: list[dict[str, Any]] = []

    _add_threshold_check(
        checks,
        "Green Area",
        actual=float(metrics.get("green_cover_pct", 0)) / 100,
        required=float(constraints.get("min_green_area_pct", 0)),
        comparator="min",
        citation=_citation(regulations, "min_green_area_pct", constraints.get("min_green_area_pct")),
        unit="%",
    )
    _add_threshold_check(
        checks,
        "Ground Coverage",
        actual=float(metrics.get("built_cover_pct", 0)) / 100,
        required=float(constraints.get("max_ground_coverage_pct", 1)),
        comparator="max",
        citation=_citation(regulations, "max_ground_coverage_pct", constraints.get("max_ground_coverage_pct")),
        unit="%",
    )
    _add_threshold_check(
        checks,
        "FAR",
        actual=float(metrics.get("far", 0)),
        required=float(constraints.get("max_far", 0)),
        comparator="max",
        citation=_citation(regulations, "max_far", constraints.get("max_far")),
        unit="",
    )
    parking_norms = constraints.get("parking_norms", {})
    required_parking = int((float(metrics.get("site_area_sqm", 0)) / 100) * float(parking_norms.get("two_wheeler_per_100sqm", 0)))
    _add_threshold_check(
        checks,
        "Two-Wheeler Parking",
        actual=float(metrics.get("parking_spaces", 0)),
        required=float(required_parking),
        comparator="min",
        citation=_citation(regulations, "parking_norms.two_wheeler_per_100sqm", parking_norms.get("two_wheeler_per_100sqm")),
        unit=" bays",
    )
    if layout_geojson:
        min_vehicle_width = _min_zone_width(layout_geojson, "vehicle")
        _add_threshold_check(
            checks,
            "Emergency Clear Width",
            actual=min_vehicle_width,
            required=float(constraints.get("fire_safety", {}).get("min_clear_access_width_m", 4.5)),
            comparator="min",
            citation=_citation(
                regulations,
                "fire_safety.min_clear_access_width_m",
                constraints.get("fire_safety", {}).get("min_clear_access_width_m", 4.5),
            ),
            unit="m",
        )

    if regulations.get("review_status") != "approved":
        checks.append(
            {
                "check": "Regulation Review",
                "status": "warning",
                "required_value": "approved",
                "actual_value": regulations.get("review_status", "unknown"),
                "detail": "Regulation values are pending human verification.",
                "source_citation": _citation(regulations, "review_status", regulations.get("review_status")),
            }
        )

    status = "valid"
    if any(check["status"] == "violation" for check in checks):
        status = "violation"
    elif any(check["status"] == "warning" for check in checks):
        status = "warning"
    return {
        "status": status,
        "checks": checks,
        "violations": [check for check in checks if check["status"] == "violation"],
        "disclaimer": LEGAL_DISCLAIMER,
    }


def _add_threshold_check(
    checks: list[dict[str, Any]],
    name: str,
    actual: float,
    required: float,
    comparator: str,
    citation: str,
    unit: str,
) -> None:
    valid = actual >= required if comparator == "min" else actual <= required
    status = "valid" if valid else "violation"
    if unit == "%":
        actual_text = f"{actual:.1%}"
        required_text = f"{required:.1%}"
    elif unit == "":
        actual_text = f"{actual:.3f}"
        required_text = f"{required:.3f}"
    else:
        actual_text = f"{actual:.2f}{unit}"
        required_text = f"{required:.2f}{unit}"
    direction = "minimum" if comparator == "min" else "maximum"
    checks.append(
        {
            "check": name,
            "status": status,
            "required_value": required_text,
            "actual_value": actual_text,
            "detail": f"{name}: actual {actual_text}; required {direction} {required_text}.",
            "source_citation": citation,
        }
    )


def _min_zone_width(layout_geojson: dict[str, Any], zone: str) -> float:
    from shapely.geometry import shape
    from engine.geo_utils import to_utm

    widths = []
    for feature in layout_geojson.get("features", []):
        props = feature.get("properties", {})
        if props.get("zone_type") == zone or props.get("zone") == zone:
            geom = to_utm(shape(feature["geometry"]))
            minx, miny, maxx, maxy = geom.bounds
            widths.append(min(maxx - minx, maxy - miny))
    return min(widths, default=0)
