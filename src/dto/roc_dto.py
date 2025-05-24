from pydantic import BaseModel
from typing import Literal


class ROCdto(BaseModel):
    type: Literal["roc"] = "roc"
    t : int
    price: float
    roc : float | str
