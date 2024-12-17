from fastapi import FastAPI
from app.routers import games

app = FastAPI()

app.include_router(games.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"hello": "world"}
