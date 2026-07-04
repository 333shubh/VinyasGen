from pathlib import Path

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    create_engine,
)
from sqlalchemy.engine import Engine

DATABASE_PATH = Path(__file__).resolve().parent / "vinyasgen.sqlite3"
DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

metadata = MetaData()

ward_projects = Table(
    "ward_projects",
    metadata,
    Column("id", String, primary_key=True),
    Column("ward_name", String),
    Column("city", String),
    Column("authority", String),
    Column("planner_name", String),
    Column("financial_year", String),
    Column("created_at", DateTime),
)

projects = Table(
    "projects",
    metadata,
    Column("project_id", String, primary_key=True),
    Column("ward_project_id", String, ForeignKey("ward_projects.id")),
    Column("user_id", String),
    Column("site_name", String),
    Column("city", String),
    Column("zone_code", String),
    Column("site_type", String),
    Column("plot_geojson", Text),
    Column("actual_geojson", Text),
    Column("total_width_m", Float),
    Column("usable_width_m", Float),
    Column("slope_direction", String),
    Column("status", String, default="boundary_drawn"),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    Index("ix_projects_city_zone", "city", "zone_code"),
    Index("ix_projects_ward_project_id", "ward_project_id"),
)

layout_options = Table(
    "layout_options",
    metadata,
    Column("layout_id", String, primary_key=True),
    Column("project_id", String, ForeignKey("projects.project_id")),
    Column("objective_profile", String),
    Column("geojson", Text),
    Column("metrics_json", Text),
    Column("slider_values_json", Text),
    Column("material_choices", Text),
    Column("phase_assignments", Text),
    Column("is_active", Integer, default=0),
    Column("created_at", DateTime),
    Index("ix_layout_options_project_id", "project_id"),
)

compliance_results = Table(
    "compliance_results",
    metadata,
    Column("result_id", String, primary_key=True),
    Column("layout_id", String, ForeignKey("layout_options.layout_id")),
    Column("check_name", String),
    Column("status", String),
    Column("required_value", String),
    Column("actual_value", String),
    Column("detail", Text),
    Column("citation", Text),
    Column("created_at", DateTime),
    Index("ix_compliance_results_layout_id", "layout_id"),
)

encroachments = Table(
    "encroachments",
    metadata,
    Column("encroachment_id", String, primary_key=True),
    Column("project_id", String, ForeignKey("projects.project_id")),
    Column("anon_label", String),
    Column("geometry_geojson", Text),
    Column("depth_m", Float),
    Column("area_sqm", Float),
    Column("detection_mode", String),
    Column("confidence", String),
    Column("verified", Integer, default=0),
    Column("created_at", DateTime),
    Index("ix_encroachments_project_id", "project_id"),
)

reports = Table(
    "reports",
    metadata,
    Column("report_id", String, primary_key=True),
    Column("layout_id", String, ForeignKey("layout_options.layout_id")),
    Column("report_type", String),
    Column("pdf_path", Text),
    Column("generated_at", DateTime),
    Index("ix_reports_layout_id", "layout_id"),
)


def get_engine(database_url: str = DATABASE_URL) -> Engine:
    return create_engine(database_url, future=True)


def initialize_database(engine: Engine | None = None) -> None:
    metadata.create_all(engine or get_engine())
