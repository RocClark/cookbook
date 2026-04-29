# backend/app/routes/tips.py

from fastapi import APIRouter, HTTPException
from app.models.tips import Tip
from app.db.json_handler import load_data, save_data, TIPS_FILE

router = APIRouter(prefix="/tips", tags=["Tips"])

@router.get("/")
def get_tips():
    return load_data(TIPS_FILE)

@router.post("/")
def create_tip(tip: Tip):
    tips = load_data(TIPS_FILE)

    tip.id = len(tips) + 1
    tips.append(tip.dict())

    save_data(TIPS_FILE, tips)

    return tip

@router.delete("/{tip_id}")
def delete_tip(tip_id: int):
    tips = load_data(TIPS_FILE)

    updated = [t for t in tips if t["id"] != tip_id]

    if len(updated) == len(tips):
        raise HTTPException(status_code=404, detail="Tip not found")

    save_data(TIPS_FILE, updated)

    return {"message": "Tip deleted"}