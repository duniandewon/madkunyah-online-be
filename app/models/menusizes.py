from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core import Base


class MenuSize(Base):
    __tablename__ = "menu_sizes"

    id = Column(Integer, primary_key=True, index=True)
    group = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

    menus = relationship("Menu", secondary="menu_menu_sizes", back_populates="sizes")
