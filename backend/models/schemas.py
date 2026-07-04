from typing import Any, Literal

from pydantic import BaseModel, Field

SiteType = Literal["empty_plot", "street_regeneration", "public_space"]


class SliderValues(BaseModel):
    density_level: float = Field(default=0.45, ge=0.0, le=1.0)
    greenery_pct: float = Field(default=0.25, ge=0.05, le=0.8)
    pedestrian_priority: float = Field(default=0.4, ge=0.0, le=1.0)


class LayoutGenerateRequest(BaseModel):
    plot_geojson: dict[str, Any] = Field(..., description="GeoJSON Feature with Polygon geometry.")
    city: str = "noida"
    zone_code: str = "residential_group_housing"
    site_type: SiteType = "empty_plot"
    context: dict[str, Any] = Field(default_factory=dict)
    slider_values: SliderValues = Field(default_factory=SliderValues)


class LayoutUpdateRequest(BaseModel):
    plot_geojson: dict[str, Any]
    city: str = "noida"
    zone_code: str = "residential_group_housing"
    site_type: SiteType = "empty_plot"
    slider_values: SliderValues = Field(default_factory=SliderValues)


class CopilotMessageRequest(BaseModel):
    project_id: str | None = None
    active_layout_id: str | None = None
    message: str


class ReportGenerateRequest(BaseModel):
    layout_option: dict[str, Any]


class CommunityVoteRequest(BaseModel):
    report_id: str
    vote_type: Literal["support", "concern", "needs_changes"]
    comment: str = ""


class DxfExportRequest(BaseModel):
    layout_option: dict[str, Any]


class LayoutOption(BaseModel):
    layout_id: str
    objective_profile: str
    geojson: dict[str, Any]
    metrics: dict[str, Any]
    compliance_summary: dict[str, Any]


class LayoutGenerateResponse(BaseModel):
    project_id: str
    layout_options: list[LayoutOption]


class CopilotMessageResponse(BaseModel):
    reply_text: str
    suggested_action: dict[str, Any] | None = None


class RegulationResponse(BaseModel):
    city: str
    zone_code: str
    regulations: dict[str, Any]
