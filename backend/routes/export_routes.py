from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from engine.dxf_exporter import layout_to_dxf
from models.schemas import DxfExportRequest

router = APIRouter()


@router.post("/dxf", response_class=PlainTextResponse)
def export_dxf(request: DxfExportRequest) -> str:
    return layout_to_dxf(request.layout_option)
