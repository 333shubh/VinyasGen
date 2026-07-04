# Regulation Researcher Guardrail

The Regulation Researcher may draft JSON into `data/pending_review/`, but cannot mark a regulation file as `approved`.

Required human checkpoint:
- Verify every numeric value against an official municipal source.
- Add page, table, or clause citation.
- Only then move reviewed JSON into `data/regulations/{city}/`.

LLM output must be structured JSON only. It must never calculate geometry, area, parking counts, or compliance status.
