from fastapi import APIRouter
from src.models.mode_model import Mode
from src.controllers.modes_controller import ModeController
from src.dto.sma_dto import SMADto
from src.dto.rl_dto import RLDto
modes_router = APIRouter()

@modes_router.post("/mode", tags=["Modes"], description='Media Móvil Simple (SMA)Crossover')
def get_sma(mode : Mode) -> SMADto:
    return ModeController.calculate_sma(mode)

@modes_router.post("/mode/two", tags=["Modes"] , description='Regresión Lineal ')
def get_mode_rl(mode: Mode) -> RLDto:
    return ModeController.calculate_rl(mode)

@modes_router.get("/mode/three", tags=["Modes"], description='Momentum (ROC)')
def get_mode_roc(mode: Mode):
    return f"hola "

