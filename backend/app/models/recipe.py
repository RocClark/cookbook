from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


# Data received from frontend
class RecipeCreate(BaseModel):
    title: str
    ingredients: List[str]
    tools: List[str] = []
    prep: List[str]
    cook: List[str]
    category: Optional[str] = None
    tags: List[str] = []


# Data saved in DB + returned
class Recipe(BaseModel):
    id: int
    title: str
    ingredients: List[str]
    tools: List[str] = []
    prep: List[str]
    cook: List[str]
    category: Optional[str] = None
    tags: List[str] = []
    created_at: datetime
    updated_at: datetime