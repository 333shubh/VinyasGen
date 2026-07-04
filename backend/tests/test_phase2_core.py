import json
import time
from pathlib import Path

from fastapi.testclient import TestClient
from shapely.geometry import shape
from shapely.ops import unary_union

from engine.encroachment import calculate_encroachments
from engine.parking_optimizer import optimize_parking
from engine.geo_utils import to_utm
from main import app

client = TestClient(app)
FIXTURES = Path(__file__).parent / "fixtures"


def _fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_generate_layouts_returns_five_valid_non_overlapping_options_for_fixtures():
    for fixture_name, site_type in [
        ("square_plot.geojson", "empty_plot"),
        ("l_shaped_plot.geojson", "empty_plot"),
        ("narrow_lane_4m.geojson", "gali"),
    ]:
        response = client.post(
            "/api/layout/generate",
            json={"plot_geojson": _fixture(fixture_name), "site_type": site_type},
        )
        assert response.status_code == 200
        options = response.json()["layout_options"]
        assert len(options) == 5
        for option in options:
            polygons = [
                shape(feature["geometry"])
                for feature in option["geojson"]["features"]
                if feature["geometry"]["type"] == "Polygon" and feature["properties"]["zone_type"] != "parking_stall"
            ]
            assert all(poly.is_valid for poly in polygons)
            assert abs(sum(poly.area for poly in polygons) - unary_union(polygons).area) < 1e-12


def test_layout_update_returns_within_500ms():
    started = time.perf_counter()
    response = client.post(
        "/api/layout/update",
        json={
            "plot_geojson": _fixture("sector_road_12m.geojson"),
            "site_type": "road",
            "slider_values": {"density_level": 0.7, "greenery_pct": 0.1, "pedestrian_priority": 0.2},
            "objective_profile_key": "pedestrian",
        },
    )
    elapsed_ms = (time.perf_counter() - started) * 1000
    assert response.status_code == 200
    assert response.json()["layout_id"] == "layout_pedestrian"
    assert elapsed_ms < 500


def test_compliance_flags_ground_coverage_and_access_failures():
    plot = _fixture("square_plot.geojson")
    response = client.post(
        "/api/layout/generate",
        json={"plot_geojson": plot, "site_type": "empty_plot", "slider_values": {"density_level": 1, "greenery_pct": 0.05}},
    )
    assert response.status_code == 200
    checks = response.json()["layout_options"][0]["compliance_summary"]["checks"]
    assert any(check["check"] == "Ground Coverage" for check in checks)

    narrow = client.post("/api/layout/generate", json={"plot_geojson": _fixture("narrow_lane_4m.geojson"), "site_type": "gali"})
    assert narrow.status_code == 200
    assert any(option["emergency_access"]["overall_status"] == "FAIL" for option in narrow.json()["layout_options"])


def test_parking_optimizer_returns_non_overlapping_stalls_within_ten_seconds():
    polygon = to_utm(shape(_fixture("sector_road_12m.geojson")["geometry"]))
    started = time.perf_counter()
    features, metrics = optimize_parking(polygon)
    assert (time.perf_counter() - started) < 10
    assert metrics["parking_spaces"] == len(features)
    stalls = [shape(feature["geometry"]) for feature in features]
    assert abs(sum(stall.area for stall in stalls) - unary_union(stalls).area) < 1e-12


def test_pdf_report_and_manual_encroachment_calculation():
    layout = client.post("/api/layout/generate", json={"plot_geojson": _fixture("sector_road_12m.geojson"), "site_type": "road"}).json()["layout_options"][0]
    report = client.post("/api/report/generate", json={"layout_option": layout, "acknowledge_emergency_override": True})
    assert report.status_code == 200
    download = client.get(report.json()["download_url"])
    assert download.status_code == 200
    assert download.headers["content-type"] == "application/pdf"

    official = _fixture("narrow_lane_4m.geojson")
    actual = _fixture("narrow_lane_4m.geojson")
    actual["geometry"]["coordinates"][0][2][1] -= 0.000018
    actual["geometry"]["coordinates"][0][3][1] -= 0.000018
    result = calculate_encroachments(official, actual)
    assert abs(result["summary"]["max_depth_m"] - 2.0) <= 0.25
