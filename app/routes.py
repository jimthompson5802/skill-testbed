# app/routes.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    """Retrieve all users"""
    return []

@router.post("/users")
def create_user():
    """Create a new user"""
    return {}