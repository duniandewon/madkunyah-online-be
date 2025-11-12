from sqlalchemy import Column, Integer, ForeignKey
from app.core import Base


class MenuOption(Base):
    __tablename__ = "menu_options"

    menu_id = Column(
        Integer, ForeignKey("menus.id", ondelete="CASCADE"), primary_key=True
    )
    option_id = Column(
        Integer, ForeignKey("options.id", ondelete="CASCADE"), primary_key=True
    )
