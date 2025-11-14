from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship

from app.core import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    image = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)

    modifier_groups = relationship(
        "ModifierGroup", secondary="menu_modifier_links", back_populates="menus"
    )
