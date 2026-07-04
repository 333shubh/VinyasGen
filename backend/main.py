from contextlib import asynccontextmanager
from datetime import UTC, datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import initialize_database
from routes.regulation_routes import router as regulation_router

LEGAL_DISCLAIMER = (
    "VinyasGen is a decision-support and visualization tool. All outputs - layouts, "
    "compliance results, cost estimates, and encroachment flags - are indicative only, "
    "based on digitized regulatory data, and do not constitute statutory approval, "
    "legal measurement, or enforcement action. All proposals must be verified with the "
    "relevant municipal authority before implementation. Encroachment flags are "
    "potential indicators requiring field verification - they do not constitute legal "
    "evidence of unauthorized construction."
)


@asynccontextmanager
async def lifespan(_: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="VinyasGen API",
    description="Deterministic geometry and regulation API for urban regeneration layouts.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check() -> dict:
    return {
        "status": "ok",
        "version": "0.1.0",
        "timestamp": datetime.now(UTC).isoformat(),
        "disclaimer": LEGAL_DISCLAIMER,
    }


app.include_router(regulation_router, prefix="/api/regulations", tags=["regulations"])
