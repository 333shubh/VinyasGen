import json
from pathlib import Path
from typing import Any

DATA_ROOT = Path(__file__).resolve().parents[2] / "data" / "regulations"


def load_regulations(city: str, zone_code: str) -> dict[str, Any]:
    path = DATA_ROOT / city.lower() / f"{zone_code}.json"
    if not path.exists():
        raise FileNotFoundError(f"No regulation JSON found for {city}/{zone_code}.")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
