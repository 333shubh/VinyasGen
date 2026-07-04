# Copilot Guardrail

The Copilot translates plain language into structured slider or constraint JSON.

It must not:
- calculate site area
- calculate compliance
- invent regulation values
- override deterministic engine output

All geometry and compliance decisions belong to the FastAPI engine.
