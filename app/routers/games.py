from fastapi import APIRouter

router = APIRouter()

# Get a game by ID
@router.get("/games/{game_id}")
async def get_game(game_id: str):
    return {"game_id": game_id}

# Create a game
@router.post("/games")
async def create_game():
    return {"message": "Game created"}
