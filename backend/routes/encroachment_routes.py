from fastapi import APIRouter, HTTPException

from engine.encroachment import calculate_encroachments
from models.schemas import EncroachmentCalculateRequest

router = APIRouter()


@router.post("/calculate")
def calculate(request: EncroachmentCalculateRequest) -> dict:
    try:
        return calculate_encroachments(request.official_geojson, request.actual_geojson)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
