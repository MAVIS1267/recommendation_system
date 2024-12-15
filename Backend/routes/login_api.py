from fastapi import APIRouter, HTTPException
from services.login_service import login

router = APIRouter()

@router.post("/user/login")
def user_login(email: str, password: str):
    """Login with email and password."""
    response = login(email, password)
    if response["status"]:
        return response["user"]
    raise HTTPException(status_code=401, detail=response["message"])