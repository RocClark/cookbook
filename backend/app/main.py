from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Cookbook API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Recipe(BaseModel):
    title: str
    ingredients: list[str]
    tools: list[str]
    prep: list[str]
    cook: list[str]

@app.get("/")
def root():
    return {"message": "Welcome to the Cookbook API!"}

@app.get("/recipes")
def get_recipes():
    return {"recipes": ["Spaghetti", "Tacos"]}

@app.post("/recipes")
def create_recipe(recipe: Recipe):
    print("Received Recipe:", recipe.dict())   # 🔥 CONFIRM FRONTEND CONNECTION
    return {"status": "ok", "received": recipe}