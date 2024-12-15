from fastapi import APIRouter, HTTPException
from services.user_service import load_users, save_users

router = APIRouter()

# Load user data
users = load_users()

@router.get("/users")
def get_all_users():
    """Get all users."""
    return users

@router.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    """Get user details by user ID."""
    user = users.get(f"user_{user_id}", None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found.")
