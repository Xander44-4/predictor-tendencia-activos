from pydantic import BaseModel, Field
from typing import Optional, List, Annotated, Union, Literal

from src.dto.rl_dto import RLDto
from src.dto.roc_dto import ROCdto
from src.dto.sma_dto import SMADto
from src.models.values_model import ValuesModel




class ROCListDto(BaseModel):
    type: Literal["roc_list"] = "roc_list"
    values: List[ROCdto]

AnswerUnion = Annotated[
    Union[SMADto, RLDto, ROCListDto],
    Field(discriminator="type")
]

class Mode(BaseModel):
    id : Optional[str] = None
    mode_type: int # 1-SMA 2-RL 3-ROC
    userId: str
    inputs : List[ValuesModel] = Field(..., min_length=20)
    answer_mode: Optional[AnswerUnion] = None





