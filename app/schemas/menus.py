from pydantic import BaseModel
from typing import Optional


class BaseMeu(BaseModel):
    name: str
    description: str | None = None
    image: str | None = None
    price: float
    category: str


class CreateMenu(BaseMeu):
    pass


class UpdateMenu(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None


class Menu(BaseMeu):
    id: int

    class Config:
        orm_mode = True
