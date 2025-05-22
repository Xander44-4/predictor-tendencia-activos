from pydantic import BaseModel

class SMADto(BaseModel):
    high_sma: float
    low_sma: float
    msg: str

    def __init__(self, high_sma: float, low_sma: float, msg: str):
        super().__init__(high_sma=high_sma, low_sma=low_sma, msg=msg)
