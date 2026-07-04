from typing import Any

LEGAL_DISCLAIMER = (
    "VinyasGen is a decision-support and visualization tool. Compliance results "
    "are indicative, based on digitized regulatory data, and do not constitute "
    "statutory approval. All proposals must be verified with the relevant "
    "municipal authority before implementation."
)


def check_layout(metrics: dict[str, Any], regulations: dict[str, Any]) -> dict[str, Any]:
    constraints = regulations.get("constraints", {})
    checks: list[dict[str, Any]] = []

    min_green = float(constraints.get("min_green_area_pct", 0))
    green_ratio = float(metrics.get("green_cover_pct", 0)) / 100
    checks.append(
        {
            "check": "Green Cover",
            "status": "valid" if green_ratio >= min_green else "violation",
            "detail": f"Green cover is {green_ratio:.0%}; minimum is {min_green:.0%}.",
            "source_citation": regulations.get("source_document", "Pending source review"),
        }
    )

    max_ground = float(constraints.get("max_ground_coverage_pct", 1))
    built_ratio = float(metrics.get("built_cover_pct", 0)) / 100
    checks.append(
        {
            "check": "Built Coverage",
            "status": "valid" if built_ratio <= max_ground else "violation",
            "detail": f"Built coverage is {built_ratio:.0%}; maximum is {max_ground:.0%}.",
            "source_citation": regulations.get("source_document", "Pending source review"),
        }
    )

    status = "valid"
    if any(check["status"] == "violation" for check in checks):
        status = "violation"
    elif regulations.get("review_status") != "approved":
        status = "warning"

    if regulations.get("review_status") != "approved":
        checks.append(
            {
                "check": "Regulation Review",
                "status": "warning",
                "detail": "Regulation values are marked pending review and must be verified before real submission.",
                "source_citation": regulations.get("source_document", "Pending source review"),
            }
        )

    return {
        "status": status,
        "checks": checks,
        "violations": [check for check in checks if check["status"] == "violation"],
        "disclaimer": LEGAL_DISCLAIMER,
    }
