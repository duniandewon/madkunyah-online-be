from pydantic import BaseModel
from typing import Optional

from .menusizes import MenuSize
from .options import Option


class BaseMenu(BaseModel):
    name: str
    description: str | None = None
    image: str | None = None
    price: float
    category: str


class CreateMenu(BaseMenu):
    pass


class UpdateMenu(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None


class Menu(BaseMenu):
    id: int
    sizes: list[MenuSize] = []
    options: list[Option] = []

    class Config:
        orm_mode = True
