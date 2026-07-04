from uuid import uuid4

from fastapi import APIRouter, HTTPException

from engine.geometry_engine import generate_layout_options
from engine.regulation_loader import load_regulations
from models.schemas import LayoutGenerateRequest, LayoutGenerateResponse, LayoutUpdateRequest

router = APIRouter()


@router.post("/generate", response_model=LayoutGenerateResponse)
def generate_layout(request: LayoutGenerateRequest) -> LayoutGenerateResponse:
    try:
        regulations = load_regulations(request.city, request.zone_code)
        options = generate_layout_options(
            request.plot_geojson,
            request.slider_values.model_dump(),
            regulations,
            request.site_type,
            request.total_width_m,
        )
        return LayoutGenerateResponse(project_id=f"proj_{uuid4().hex[:8]}", layout_options=options)
    except (FileNotFoundError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/update")
def update_layout(request: LayoutUpdateRequest) -> dict:
    try:
        regulations = load_regulations(request.city, request.zone_code)
        options = generate_layout_options(
            request.plot_geojson,
            request.slider_values.model_dump(),
            regulations,
            request.site_type,
            request.total_width_m,
        )
        if request.objective_profile_key:
            for option in options:
                if option["layout_id"] == f"layout_{request.objective_profile_key}":
                    return option
        return options[0]
    except (FileNotFoundError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
