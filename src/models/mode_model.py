from pydantic import BaseModel, Field, conlist
from typing import Optional, List , Annotated
from src.models.values_model import ValuesModel

class Mode(BaseModel):
    id : Optional[str]
    mode_type: int # 1-SMA 2-RL 3-ROC
    userId: str
    inputs : List[ValuesModel] = Field(..., min_length=20)




