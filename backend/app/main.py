from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import recipes

app = FastAPI(title="Cookbook API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router)


@app.get("/")
def root():
    return {"message": "Cookbook API is running"}