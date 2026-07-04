import json
from pathlib import Path

from fastapi.testclient import TestClient
from shapely.geometry import shape

from engine.geo_utils import to_utm
from main import app

client = TestClient(app)
FIXTURES = Path(__file__).parent / "fixtures"


def _fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def _area_by_zone(layout: dict, zone_type: str) -> float:
    area = 0.0
    for feature in layout["geojson"]["features"]:
        props = feature.get("properties", {})
        if props.get("zone_type") != zone_type:
            continue
        area += to_utm(shape(feature["geometry"])).area
    return area


def test_layout_metrics_are_derived_from_rendered_geojson():
    boundary = _fixture("square_plot.geojson")
    response = client.post(
        "/api/layout/generate",
        json={"plot_geojson": boundary, "site_type": "empty_plot"},
    )

    assert response.status_code == 200
    layout = response.json()["layout_options"][0]
    metrics = layout["metrics"]
    site_area = to_utm(shape(boundary["geometry"])).area
    rendered_green_area = _area_by_zone(layout, "green") + _area_by_zone(layout, "open_space")
    rendered_building_area = _area_by_zone(layout, "building")
    rendered_parking_count = sum(
        1
        for feature in layout["geojson"]["features"]
        if feature.get("properties", {}).get("zone_type") == "parking_stall"
    )

    assert abs(metrics["green_area_sqm"] - rendered_green_area) < 0.1
    assert abs(metrics["ground_coverage_area_sqm"] - rendered_building_area) < 0.1
    assert abs(metrics["green_cover_pct"] - round((rendered_green_area / site_area) * 100, 1)) < 0.1
    assert abs(metrics["built_cover_pct"] - round((rendered_building_area / site_area) * 100, 1)) < 0.1
    assert metrics["parking_spaces"] == rendered_parking_count
    assert abs(metrics["floor_area_sqm"] - rendered_building_area) < 0.1
    assert abs(metrics["far"] - round(rendered_building_area / site_area, 3)) < 0.001


def test_far_compliance_uses_calculated_metric_and_citation():
    response = client.post(
        "/api/layout/generate",
        json={"plot_geojson": _fixture("square_plot.geojson"), "site_type": "empty_plot"},
    )

    checks = response.json()["layout_options"][0]["compliance_summary"]["checks"]
    far_check = next(check for check in checks if check["check"] == "FAR")

    assert far_check["actual_value"] != "0.000"
    assert "max_far" in far_check["source_citation"]
    assert far_check["required_value"] != "0.000"
