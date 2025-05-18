from fastapi import APIRouter
from fastapi.responses import JSONResponse

modes_router = APIRouter()

@modes_router.get("/mode", tags=["Modes"])
def get_mode_one(one : str):
    return f"hola {one}"

@modes_router.get("/mode/two", tags=["Modes"])
def get_mode_two(one : str):
    return f"hola {one}"

@modes_router.get("/mode/three", tags=["Modes"])
def get_mode_three(one : str):
    return f"hola {one}"




