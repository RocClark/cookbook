# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import recipes, tips

app = FastAPI(title="Cookbook API", version="1.0")

# ✅ Enable CORS so Next.js can talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(recipes.router)
app.include_router(tips.router)

@app.get("/")
def root():
    return {"message": "Cookbook API is running"}