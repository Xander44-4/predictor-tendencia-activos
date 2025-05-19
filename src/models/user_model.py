from pydantic import BaseModel, field_validator ,Field , EmailStr
from typing import Optional
class User(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    username: str = Field(min_length=3, max_length=20)
    age: int = Field(ge = 18)
    email: EmailStr
    password_hashed: str


