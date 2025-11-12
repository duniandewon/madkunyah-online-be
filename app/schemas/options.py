from pydantic import BaseModel
from typing import Optional


class OptionBase(BaseModel):
    name: str
    price: float


class CreateOption(OptionBase):
    pass


class UpdateOption(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


class Option(OptionBase):
    id: int

    class Config:
        from_attributes = True
