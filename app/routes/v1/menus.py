from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.menus import Menu, CreateMenu, UpdateMenu
from app.core.db import get_session

from app.services import menus

router = APIRouter()


@router.get("/", response_model=List[Menu])
async def get_all_menus(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_session),
):
    return await menus.get_all_menus(db, skip, limit)


@router.post("/", response_model=Menu)
async def create_menu(menu: CreateMenu, db: AsyncSession = Depends(get_session)):
    return await menus.create_menu(db, menu)


@router.get("/{menu_id}", response_model=Menu)
async def get_menu_by_id(menu_id: int, db: AsyncSession = Depends(get_session)):
    menu = await menus.get_menu_by_id(db, menu_id)

    if not menu:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu


@router.patch("/{item_id}", response_model=Menu)
async def update_menu(
    menu_id: int, menu: UpdateMenu, db: AsyncSession = Depends(get_session)
):
    updated = await menus.update_menu(db, menu_id, menu)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@router.delete("/{menu_id}")
async def delete_menu(menu_id: int, db=Depends(get_session)):
    deleted = await menus.delete_menu(db, menu_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Deleted"}


@router.post("/{menu_id}/add-size/{menus_size_id}")
async def add_menu_size(menu_id: int, menu_size_id: int, db=Depends(get_session)):
    updated = await menus.add_size_to_menu(db, menu_id, menu_size_id)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@router.delete("/{menu_id}/add-size/{menus_size_id}")
async def remove_menu_size(menu_id: int, menu_size_id: int, db=Depends(get_session)):
    updated = await menus.remove_size_from_menu(db, menu_id, menu_size_id)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@router.post("/{menu_id}/add-size/{option_id}")
async def add_options(menu_id: int, option_id: int, db=Depends(get_session)):
    updated = await menus.add_option_to_menu(db, menu_id, option_id)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@router.delete("/{menu_id}/add-size/{option_id}")
async def remove_options(menu_id: int, option_id: int, db=Depends(get_session)):
    updated = await menus.remove_option_from_menu(db, menu_id, option_id)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated
