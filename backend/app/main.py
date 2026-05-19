from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.recipe import Recipe, RecipeCreate
import json
import os
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = "data/recipes.json"


def load_recipes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_recipes(recipes):
    with open(DATA_FILE, "w") as f:
        json.dump(recipes, f, indent=2)


@app.get("/recipes")
def get_recipes():
    return load_recipes()


@app.post("/recipes")
def create_recipe(recipe_data: RecipeCreate):
    recipes = load_recipes()

    # Generate new ID
    new_id = max([r["id"] for r in recipes], default=0) + 1

    now = datetime.utcnow()

    new_recipe = Recipe(
        id=new_id,
        created_at=now,
        updated_at=now,
        **recipe_data.dict()
    )

    recipes.append(new_recipe.dict())
    save_recipes(recipes)

    return {"message": "Recipe saved!", "recipe": new_recipe}