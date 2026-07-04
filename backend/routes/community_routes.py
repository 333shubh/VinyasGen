from collections import defaultdict
from uuid import uuid4

from fastapi import APIRouter

from models.schemas import CommunityVoteRequest

router = APIRouter()

_votes: dict[str, list[dict]] = defaultdict(list)


@router.post("/vote")
def submit_vote(request: CommunityVoteRequest) -> dict:
    vote = {
        "vote_id": f"vote_{uuid4().hex[:10]}",
        "report_id": request.report_id,
        "vote_type": request.vote_type,
        "comment": request.comment,
    }
    _votes[request.report_id].append(vote)
    return {"status": "saved", "vote": vote}


@router.get("/{report_id}/votes")
def get_votes(report_id: str) -> dict:
    votes = _votes[report_id]
    summary = {
        "support": sum(1 for vote in votes if vote["vote_type"] == "support"),
        "concern": sum(1 for vote in votes if vote["vote_type"] == "concern"),
        "needs_changes": sum(1 for vote in votes if vote["vote_type"] == "needs_changes"),
    }
    return {"report_id": report_id, "summary": summary, "votes": votes}
