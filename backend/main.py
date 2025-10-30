from fastapi import FastAPI

app = FastAPI(title="Cookbook API", version="1.0")

@app.get("/")
def root():
    return {"message": "Welcome to the Cookbook API!"}

@app.get("/recipes")
def get_recipes():
    return {"recipes": ["Spaghetti Bolognese", "Chicken Alfredo", "Tacos"]}

@app.get("/tips")
def get_tips():
    return {"tips": ["Use fresh herbs", "Don’t overcook pasta", "Taste as you go"]}
