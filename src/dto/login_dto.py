from pydantic import BaseModel, field_validator ,Field , EmailStr


class UserDto(BaseModel):
    email: EmailStr
    password_hashed: str