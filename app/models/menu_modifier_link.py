from sqlalchemy import Column, Integer, ForeignKey

from app.core import Base


class MenuModifierLink(Base):
    __tablename__ = "menu_modifier_links"

    id = Column(Integer, primary_key=True, index=True)
    menu_id = Column(Integer, ForeignKey("menus.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("modifier_group.id"), nullable=False)
