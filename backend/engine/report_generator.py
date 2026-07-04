from pathlib import Path
from uuid import uuid4

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from engine.compliance_checker import LEGAL_DISCLAIMER

EXPORT_ROOT = Path(__file__).resolve().parents[2] / "exports"
EXPORT_ROOT.mkdir(exist_ok=True)


def generate_pdf_report(layout: dict) -> tuple[str, Path]:
    report_id = f"report_{uuid4().hex[:10]}"
    path = EXPORT_ROOT / f"{report_id}.pdf"
    metrics = layout.get("metrics", {})
    compliance = layout.get("compliance_summary", {})
    styles = getSampleStyleSheet()
    story = [
        Paragraph("VinyasGen Proposal Report", styles["Title"]),
        Spacer(1, 12),
        Paragraph(f"Layout: {layout.get('objective_profile', 'Selected layout')}", styles["Heading2"]),
        Paragraph(f"Site area: {metrics.get('site_area_sqm', 'n/a')} sqm", styles["BodyText"]),
        Paragraph(f"Green Cover: {metrics.get('green_cover_pct', 'n/a')}%", styles["BodyText"]),
        Paragraph(f"Built Coverage: {metrics.get('built_cover_pct', 'n/a')}%", styles["BodyText"]),
        Paragraph(f"Organized parking: {metrics.get('parking_spaces', 'n/a')} spaces", styles["BodyText"]),
        Paragraph(f"Trees: {metrics.get('tree_count', 'n/a')}", styles["BodyText"]),
        Paragraph(f"Livability Score: {metrics.get('livability_score', 'n/a')}/100", styles["BodyText"]),
        Spacer(1, 12),
        Paragraph("Compliance Summary", styles["Heading2"]),
        Paragraph(f"Overall status: {compliance.get('status', 'n/a')}", styles["BodyText"]),
    ]
    for check in compliance.get("checks", []):
        story.append(Paragraph(f"{check.get('check')}: {check.get('detail')}", styles["BodyText"]))

    story.extend(
        [
            Spacer(1, 12),
            Paragraph("Disclaimer", styles["Heading2"]),
            Paragraph(LEGAL_DISCLAIMER, styles["BodyText"]),
        ]
    )
    SimpleDocTemplate(str(path), pagesize=A4).build(story)
    return report_id, path
