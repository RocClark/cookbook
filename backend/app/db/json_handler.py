# backend/app/db/json_handler.py
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # backend/app/db
DATA_DIR = os.path.join(BASE_DIR, "../data")            # backend/app/data
DATA_DIR = os.path.abspath(DATA_DIR)

RECIPES_FILE = os.path.join(DATA_DIR, "recipes.json")


def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return json.load(f)


def save_data(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4, default=str)