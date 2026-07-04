from typing import Any


def compute_livability_score(metrics: dict[str, Any]) -> int:
    green = min(float(metrics.get("green_cover_pct", 0)), 45) / 45
    walking = min(float(metrics.get("walking_priority", 0)), 45) / 45
    parking = min(float(metrics.get("parking_spaces", 0)), 20) / 20
    score = (green * 42) + (walking * 34) + (parking * 24)
    return round(score)
