# backend/app/routes/recipes.py

from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.recipe import Recipe, RecipeCreate
from app.db.json_handler import load_data, save_data, RECIPES_FILE

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.get("/")
def get_recipes():
    return load_data(RECIPES_FILE)

@router.get("/{recipe_id}")
def get_recipe(recipe_id: int):
    recipes = load_data(RECIPES_FILE)
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return recipe

@router.post("/")
def create_recipe(recipe_data: RecipeCreate):
    recipes = load_data(RECIPES_FILE)

    new_recipe = Recipe(
        id=len(recipes) + 1,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        **recipe_data.dict()
    )

    recipes.append(new_recipe.dict())
    save_data(RECIPES_FILE, recipes)

    return new_recipe

@router.put("/{recipe_id}")
def update_recipe(recipe_id: int, updated_recipe: Recipe):
    recipes = load_data(RECIPES_FILE)

    for i, r in enumerate(recipes):
        if r["id"] == recipe_id:
            updated_recipe.updated_at = datetime.now()
            recipes[i] = updated_recipe.dict()
            save_data(RECIPES_FILE, recipes)
            return updated_recipe

    raise HTTPException(status_code=404, detail="Recipe not found")

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int):
    recipes = load_data(RECIPES_FILE)

    updated = [r for r in recipes if r["id"] != recipe_id]

    if len(updated) == len(recipes):
        raise HTTPException(status_code=404, detail="Recipe not found")

    save_data(RECIPES_FILE, updated)

    return {"message": "Recipe deleted"}