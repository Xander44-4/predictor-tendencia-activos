from fastapi import APIRouter
from typing import List

from src.dto.roc_dto import ROCdto
from src.models.mode_model import Mode
from src.controllers.modes_controller import ModeController
from src.dto.sma_dto import SMADto
from src.dto.rl_dto import RLDto
modes_router = APIRouter()

@modes_router.post("/mode", tags=["Modes"], description='Media Móvil Simple (SMA)Crossover')
def get_sma(mode : Mode, user_id : str) -> SMADto:

    return ModeController.calculate_sma(mode, user_id)

@modes_router.post("/mode/two", tags=["Modes"] , description='Regresión Lineal ')
def get_mode_rl(mode: Mode, user_id : str) -> RLDto :

    return ModeController.calculate_rl(mode, user_id )

@modes_router.post("/mode/three", tags=["Modes"], description='Momentum (ROC)')
def get_mode_roc(mode: Mode, user_id : str,period: int = 5, )  -> List[ROCdto]:
    mode.mode_type = 3
    return ModeController.calculate_roc(mode, user_id, period)

