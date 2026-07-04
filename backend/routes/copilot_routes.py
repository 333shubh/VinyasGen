from fastapi import APIRouter

from models.schemas import CopilotMessageRequest, CopilotMessageResponse

router = APIRouter()


@router.post("/message", response_model=CopilotMessageResponse)
def copilot_message(request: CopilotMessageRequest) -> CopilotMessageResponse:
    message = request.message.lower()
    if "green" in message or "tree" in message or "park" in message:
        return CopilotMessageResponse(
            reply_text="I can increase Green Cover and keep the final check with the deterministic engine.",
            suggested_action={
                "type": "slider_update",
                "payload": {"greenery_pct": 0.4, "pedestrian_priority": 0.5},
            },
        )
    if "parking" in message or "car" in message:
        return CopilotMessageResponse(
            reply_text="I can try a parking-focused option, but compliance and area counts still come from the backend engine.",
            suggested_action={
                "type": "slider_update",
                "payload": {"density_level": 0.55, "greenery_pct": 0.18, "pedestrian_priority": 0.3},
            },
        )
    if "walk" in message or "footpath" in message or "safe" in message:
        return CopilotMessageResponse(
            reply_text="I can prioritise walking space and ask the engine to regenerate the layout.",
            suggested_action={
                "type": "slider_update",
                "payload": {"pedestrian_priority": 0.7, "greenery_pct": 0.3},
            },
        )
    return CopilotMessageResponse(
        reply_text="Tell me whether you want more Green Cover, more organized parking, or safer walking space. I will only suggest structured slider changes; the engine does the calculations.",
        suggested_action=None,
    )
