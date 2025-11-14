from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core import Base


class ModifierItem(Base):
    __tablename__ = "modifier_item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

    group_id = Column(Integer, ForeignKey("modifier_group.id"), nullable=False)

    group = relationship("ModifierGroup", back_populates="items")