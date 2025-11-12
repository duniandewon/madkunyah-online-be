from pydantic import BaseModel
from typing import Optional


class MenuSizeBase(BaseModel):
    name: str
    price: float
    group: str


class CreateMenuSize(MenuSizeBase):
    pass


class UpdateMenuSize(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    group: Optional[str] = None


class MenuSize(MenuSizeBase):
    id: int

    class Config:
        from_attributes = True
