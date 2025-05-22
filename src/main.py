from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.modes_router import modes_router
from src.routers.users_router import users_router

app = FastAPI(title="Predictor Tendencia de Activo ")
app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(router=modes_router)
app.include_router(router=users_router)



