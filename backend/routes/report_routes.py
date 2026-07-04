from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse

from engine.compliance_checker import LEGAL_DISCLAIMER
from engine.report_generator import EXPORT_ROOT, generate_pdf_report
from models.schemas import ReportGenerateRequest

router = APIRouter()


@router.post("/generate")
def generate_report(request: ReportGenerateRequest) -> dict:
    access = request.layout_option.get("emergency_access", {})
    if access.get("overall_status") == "FAIL" and not request.acknowledge_emergency_override:
        raise HTTPException(
            status_code=409,
            detail="Emergency access violations must be resolved or explicitly acknowledged before PDF export.",
        )
    report_id, _ = generate_pdf_report(request.layout_option)
    return {"report_id": report_id, "download_url": f"/api/report/{report_id}"}


@router.post("/text", response_class=PlainTextResponse)
def generate_text_report(request: ReportGenerateRequest) -> str:
    layout = request.layout_option
    metrics = layout.get("metrics", {})
    compliance = layout.get("compliance_summary", {})
    checks = compliance.get("checks", [])
    check_lines = "\n".join(
        f"- {check.get('check')}: {check.get('status')} - {check.get('detail')} ({check.get('source_citation', 'n/a')})"
        for check in checks
    )
    return f"""VinyasGen Proposal Report

Layout: {layout.get("objective_profile", "Selected layout")}

Site Overview
- Site area: {metrics.get("site_area_sqm", "n/a")} sqm
- Green Cover: {metrics.get("green_cover_pct", "n/a")}%
- Organized parking spaces: {metrics.get("parking_spaces", "n/a")}
- Emergency Access: {metrics.get("emergency_access", "n/a")}

Compliance Summary
Overall status: {compliance.get("status", "n/a")}
{check_lines}

Disclaimer
{LEGAL_DISCLAIMER}
"""


@router.post("/pdf")
def generate_pdf(request: ReportGenerateRequest) -> dict:
    return generate_report(request)


@router.get("/{report_id}")
def download_report(report_id: str) -> FileResponse:
    path = EXPORT_ROOT / f"{report_id}.pdf"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Report not found")
    return FileResponse(path, media_type="application/pdf", filename=f"{report_id}.pdf")
