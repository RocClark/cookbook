from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Incoming data from user
class RecipeCreate(BaseModel):
    title: str
    ingredients: List[str]
    instructions: str
    category: Optional[str] = None
    tags: List[str] = []

# Saved data with metadata
class Recipe(RecipeCreate):
    id: int
    created_at: datetime
    updated_at: datetime