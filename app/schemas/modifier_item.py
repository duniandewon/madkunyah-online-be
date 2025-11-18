from pydantic import BaseModel
from typing import Optional


class BaseModifierItem(BaseModel):
    name: str
    price: float


class CreateModifierItem(BaseModifierItem):
    group_id: int


class UpdateModifierItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


class ModifierItem(BaseModifierItem):
    id: int

    class Config:
        orm_mode = True
