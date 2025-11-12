from sqlalchemy import Column, Integer, ForeignKey

from app.core import Base


class MenuMenuSize(Base):
    __tablename__ = "menu_menu_sizes"

    menu_id = Column(
        Integer, ForeignKey("menus.id", ondelete="CASCADE"), primary_key=True
    )
    menu_size_id = Column(
        Integer, ForeignKey("menu_sizes.id", ondelete="CASCADE"), primary_key=True
    )
