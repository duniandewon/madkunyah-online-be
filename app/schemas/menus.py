from pydantic import BaseModel
from typing import Optional

from .modifier_group import ModifierGroup


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


class MenuSimple(BaseMenu):
    id: int

    class Config:
        orm_mode = True


class Menu(BaseMenu):
    id: int
    modifiers: list[ModifierGroup] = []

    class Config:
        orm_mode = True
