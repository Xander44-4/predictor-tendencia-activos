from pydantic import BaseModel
from typing import Optional, Literal

class SMADto(BaseModel):
    type: Literal["sma"] = "sma"
    high_sma: float
    low_sma: float
    msg: str


