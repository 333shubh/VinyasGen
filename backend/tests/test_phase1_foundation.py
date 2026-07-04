from datetime import datetime
from pathlib import Path

from fastapi.testclient import TestClient
from sqlalchemy import inspect

from database import get_engine, initialize_database
from main import app

client = TestClient(app)


def test_health_check_returns_phase1_contract():
    response = client.get("/api/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["version"] == "0.1.0"
    assert datetime.fromisoformat(body["timestamp"])
    assert "do not constitute statutory approval" in body["disclaimer"]


def test_noida_regulations_load_full_json():
    response = client.get("/api/regulations/noida/residential_group_housing")

    assert response.status_code == 200
    body = response.json()
    assert body["city"] == "noida"
    assert body["zone_code"] == "residential_group_housing"
    assert body["review_status"] == "pending_review"
    assert "constraints" in body


def test_delhi_regulations_are_distinct_from_noida():
    noida = client.get("/api/regulations/noida/residential_group_housing").json()
    delhi = client.get("/api/regulations/delhi/residential_colony").json()

    assert delhi["city"] == "delhi"
    assert delhi["zone_code"] == "residential_colony"
    assert delhi["authority"] != noida["authority"]


def test_missing_regulation_returns_404():
    response = client.get("/api/regulations/noida/not_a_zone")

    assert response.status_code == 404


def test_section_8_core_tables_are_initialized_in_sqlite(tmp_path: Path):
    database_url = f"sqlite:///{(tmp_path / 'phase1.sqlite3').as_posix()}"
    engine = get_engine(database_url)

    initialize_database(engine)

    tables = set(inspect(engine).get_table_names())
    assert {
        "projects",
        "layout_options",
        "compliance_results",
        "encroachments",
        "reports",
        "ward_projects",
    }.issubset(tables)
