from fastapi import APIRouter
from typing import List

from src.dto.roc_dto import ROCdto
from src.models.mode_model import Mode
from src.controllers.modes_controller import ModeController
from src.dto.sma_dto import SMADto
from src.dto.rl_dto import RLDto
modes_router = APIRouter()

@modes_router.post("/mode", tags=["Modes"], description='Media Móvil Simple (SMA)Crossover')
def get_sma(mode : Mode) -> SMADto:

    return ModeController.calculate_sma(mode, )

@modes_router.post("/mode/two", tags=["Modes"] , description='Regresión Lineal ')
def get_mode_rl(mode: Mode) -> RLDto :

    return ModeController.calculate_rl(mode )

@modes_router.post("/mode/three", tags=["Modes"], description='Momentum (ROC)')
def get_mode_roc(mode: Mode, period: int = 5, )  -> List[ROCdto]:
    mode.mode_type = 3
    return ModeController.calculate_roc(mode, period)

@modes_router.get("/history/{user_id}", tags=["Modes"], description='this is for wathcing the history of modes used by user')
def get_history(user_id : str):
    return ModeController.get_history(user_id)

