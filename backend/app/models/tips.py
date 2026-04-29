# backend/app/models/tip.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

class Tip(BaseModel):
    id: int
    title: str
    content: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None