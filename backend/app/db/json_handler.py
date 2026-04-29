# backend/app/db/json_handler.py

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

RECIPES_FILE = DATA_DIR / "recipes.json"
TIPS_FILE = DATA_DIR / "tips.json"

def load_data(file_path):
    if not file_path.exists():
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default=str)