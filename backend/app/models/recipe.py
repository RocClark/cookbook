# backend/app/models/recipe.py

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Recipe(BaseModel):
    id: int
    title: str
    ingredients: List[str]
    instructions: str
    category: Optional[str] = None
    tags: List[str] = []
    created_at: datetime
    updated_at: datetime