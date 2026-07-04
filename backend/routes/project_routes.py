from __future__ import annotations

import json
from datetime import UTC, datetime
from uuid import uuid4

from fastapi import APIRouter

from database import get_engine, projects
from models.schemas import ProjectCreateRequest

router = APIRouter()


@router.post("/create")
def create_project(request: ProjectCreateRequest) -> dict:
    now = datetime.now(UTC).replace(tzinfo=None)
    project_id = f"proj_{uuid4().hex[:10]}"
    record = {
        "project_id": project_id,
        "site_name": request.site_name,
        "city": request.city,
        "zone_code": request.zone_code,
        "site_type": request.site_type,
        "plot_geojson": json.dumps(request.plot_geojson),
        "actual_geojson": json.dumps(request.actual_geojson) if request.actual_geojson else None,
        "total_width_m": request.total_width_m,
        "usable_width_m": request.usable_width_m,
        "slope_direction": request.slope_direction,
        "status": "boundary_drawn",
        "created_at": now,
        "updated_at": now,
    }
    with get_engine().begin() as connection:
        connection.execute(projects.insert().values(**record))
    return {"project_id": project_id, "status": "created"}
