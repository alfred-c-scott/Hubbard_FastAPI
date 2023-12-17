from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    id: Optional[int] = None


class City(BaseModel):
    zip_code: str
    city_name: str
    state_name: str
    state_code: str
    latitude: float
    longitude: float
