from fastapi import APIRouter, HTTPException

from engine.regulation_loader import load_regulations

router = APIRouter()


@router.get("/{city}/{zone_code}")
def get_regulations(city: str, zone_code: str) -> dict:
    try:
        return load_regulations(city, zone_code)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
