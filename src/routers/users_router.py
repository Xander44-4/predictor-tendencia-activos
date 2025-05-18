from fastapi import APIRouter

users_router = APIRouter()

@users_router.post("/login")
def login(email : str, password_hash : str):
    return f"Login successful! Welcome {email} "
@users_router.post("/signup")
def signup(username : str, age : int,email : str ,password_hash : str):
    return f"Sign up successful! Welcome {username} "

@users_router.get("/get/users")
def get_users():
    return "lista de usuarios"
