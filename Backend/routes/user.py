from fastapi import APIRouter, HTTPException
from services.user_service import load_users, save_users, authenticate_user

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

@router.post("/users/authenticate")
def authenticate(username: str, password: str):
    """Authenticate a user by username and password."""
    response = authenticate_user(username, password, users)
    if response["message"] == "Authentication successful.":
        return response
    raise HTTPException(status_code=401, detail=response["message"])
