# Cookbook backend

FastAPI service backing the Cookbook app. Recipes and tips are currently
stored as JSON files under `app/data/` (a future phase migrates this to a
real database).

## Setup

From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

## Running

```bash
source .venv/bin/activate
cd backend
uvicorn app.main:app --reload
```

The API is served at `http://127.0.0.1:8000`.

## Project layout

- `app/main.py` — FastAPI app setup, CORS, router registration
- `app/routes/` — API endpoints
- `app/models/` — Pydantic request/response models
- `app/db/json_handler.py` — JSON file read/write helpers
- `app/data/` — the JSON files acting as the data store
