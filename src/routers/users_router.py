from fastapi import APIRouter, HTTPException
from starlette import status

from src.controllers.user_controller import UserController
from src.models.user_model import User
from src.dto.login_dto import UserDto
from bson import ObjectId
users_router = APIRouter()

@users_router.post("/login", tags=["Users"])
def login(login_data: UserDto):
     result= UserController.login(login_data)
     if result is None:
         raise HTTPException(
             status_code=status.HTTP_401_UNAUTHORIZED,
             detail="Credenciales inválidas"
         )
     return result
@users_router.post("/signup", tags=["Users"])
def signup(user : User):
    return UserController.create_user(user)

@users_router.get("/get/users", tags=["Users"])
def get_users():
    return UserController.get_users()


