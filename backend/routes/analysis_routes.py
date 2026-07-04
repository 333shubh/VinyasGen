from fastapi import APIRouter, HTTPException

from engine.access_checker import check_emergency_access
from engine.regulation_loader import load_regulations
from models.schemas import EmergencyAccessRequest

router = APIRouter()


@router.post("/emergency-access")
def emergency_access(request: EmergencyAccessRequest) -> dict:
    try:
        regulations = load_regulations(request.city, request.zone_code)
        return check_emergency_access(request.layout_geojson, regulations.get("constraints", {}))
    except (FileNotFoundError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
