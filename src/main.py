from fastapi import FastAPI

from src.routers.modes_router import modes_router
from src.routers.users_router import users_router

app = FastAPI(title="Predictor Tendencia de Activo ")
app.include_router(router=modes_router)
app.include_router(router=users_router)



