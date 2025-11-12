from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.core import Base


class Option(Base):
    __tablename__ = "options"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)

    menus = relationship("Menu", secondary="menu_options", back_populates="options")
