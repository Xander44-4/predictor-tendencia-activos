from pydantic import BaseModel
from typing import Literal

class RLDto(BaseModel):
    type: Literal["rl"] = "rl"
    future_value: float
    msg: str

    def __init__(self, future_value: float, msg: str):
        super().__init__(future_value = future_value, msg=msg)
