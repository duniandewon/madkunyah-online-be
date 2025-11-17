from pydantic import BaseModel
from typing import Optional

from .modifier_item import ModifierItem


class BaseModifierGroup(BaseModel):
    name: str
    type: str
    min_select: int = 0
    max_select: int = 1


class CreateModifierGroup(BaseModifierGroup):
    pass


class UpdateModifierGroup(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    min_select: Optional[int] = None
    max_select: Optional[int] = None


class ModifierGroup(BaseModifierGroup):
    id: int
    items: list[ModifierItem] = []

    class Config:
        from_attributes = True


class ModifierGroupSimple(BaseModifierGroup):
    id: int

    class Config:
        from_attributes = True
