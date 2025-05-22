from typing import List
from datetime import datetime
from pydantic import BaseModel, Field


class ValuesModel(BaseModel):
    value: int
    datetime : datetime


