from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core import Base


class ModifierGroup(Base):
    __tablename__ = "modifier_group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    min_select = Column(Integer, default=0, nullable=False)
    max_select = Column(Integer, default=1, nullable=False)

    items = relationship("ModifierItem", back_populates="group")

    menus = relationship(
        "Menu", secondary="menu_modifier_links", back_populates="modifier_groups"
    )
