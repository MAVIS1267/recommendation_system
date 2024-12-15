from fastapi import APIRouter, HTTPException
from services.history_service import load_user_watch_history, save_user_watch_history, add_movie_to_history

router = APIRouter()

# Load user watch history
user_history = load_user_watch_history()

@router.get("/history/{user_id}")
def get_user_history(user_id: int):
    """Get the watch history of a user."""
    user_id = str(user_id)
    if user_id in user_history:
        return {"user_id": user_id, "watch_history": user_history[user_id]}
    raise HTTPException(status_code=404, detail="User not found or no watch history available.")

@router.post("/history/{user_id}/add")
def add_movie(user_id: int, movie_title: str):
    """Add a movie to the user's watch history."""
    global user_history
    response = add_movie_to_history(user_id, movie_title, user_history)
    save_user_watch_history(user_history)
    return {"message": response}
