from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse

from engine.compliance_checker import LEGAL_DISCLAIMER
from engine.report_generator import EXPORT_ROOT, generate_pdf_report
from models.schemas import ReportGenerateRequest

router = APIRouter()


@router.post("/generate", response_class=PlainTextResponse)
def generate_report(request: ReportGenerateRequest) -> str:
    layout = request.layout_option
    metrics = layout.get("metrics", {})
    compliance = layout.get("compliance_summary", {})
    checks = compliance.get("checks", [])
    check_lines = "\n".join(
        f"- {check.get('check')}: {check.get('status')} - {check.get('detail')}"
        for check in checks
    )

    return f"""VinyasGen Proposal Report

Layout: {layout.get("objective_profile", "Selected layout")}

Site Overview
- Site area: {metrics.get("site_area_sqm", "n/a")} sqm
- Green Cover: {metrics.get("green_cover_pct", "n/a")}%
- Built Coverage: {metrics.get("built_cover_pct", "n/a")}%
- Organized parking spaces: {metrics.get("parking_spaces", "n/a")}
- Estimated cost: Rs {metrics.get("estimated_cost_lakh", "n/a")} lakh

Compliance Summary
Overall status: {compliance.get("status", "n/a")}
{check_lines}

Disclaimer
{LEGAL_DISCLAIMER}
"""


@router.post("/pdf")
def generate_pdf(request: ReportGenerateRequest) -> dict:
    report_id, path = generate_pdf_report(request.layout_option)
    return {"report_id": report_id, "download_url": f"/api/report/{report_id}"}


@router.get("/{report_id}")
def download_report(report_id: str) -> FileResponse:
    path = EXPORT_ROOT / f"{report_id}.pdf"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Report not found")
    return FileResponse(path, media_type="application/pdf", filename=f"{report_id}.pdf")
