from typing import List
from datetime import date
from pydantic import BaseModel, Field


class ValuesModel(BaseModel):
    value: float
    datetime : date


