# VinyasGen

Generative Intelligence for Urban Regeneration.

This repository follows `docs/VinyasGen_v2_Manifesto.md` as the single source of truth. The older `docs/VinyasGen_Report.md` is retained as historical v1 material only.

Work must follow the phase order in the v2 manifesto:

1. Phase 1 — Foundation
2. Phase 2 — Core Engines
3. Phase 3 — Differentiator Features
4. Phase 4 — Intelligence Layer
5. Phase 5 — Polish & Scale

Before starting a later phase, complete the previous phase and record its status in `docs/PHASE_LOG.md`.

Current implementation target: Phase 1 only. The app lets a planner draw an official site boundary, select a city and zone, load editable regulation JSON, and verify the backend health round trip. Layout generation, reports, encroachment analysis, and AI workflows belong to later phases.

## Run Locally

Backend:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

## Phase 1 Verification

Backend:

```bash
cd backend
python -m pytest
```

Frontend:

```bash
cd frontend
npm run build
```

## Legal Disclaimer

VinyasGen is a decision-support and visualization tool. Compliance results are indicative, based on digitized regulatory data, and do not constitute statutory approval. All proposals must be verified with the relevant municipal authority before implementation.
