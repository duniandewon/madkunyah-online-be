from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import MenuSize, CreateMenuSize, UpdateMenuSize

from app.core.db import get_session

from app.services import menussizes

router = APIRouter()


@router.get("/", response_model=List[MenuSize])
async def get_menu_sizes(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)
):
    return await menussizes.get_all_menu_size(db, skip, limit)


@router.post("/", response_model=MenuSize)
async def create_menu_size(
    menu_size: CreateMenuSize, db: AsyncSession = Depends(get_session)
):
    return await menussizes.create_menu_size(db, menu_size)


@router.get("/{menu_size_id}", response_model=MenuSize)
async def get_menu_size_by_id(
    menu_size_id: int, db: AsyncSession = Depends(get_session)
):
    menu_size = await menussizes.get_menu_by_id(db, menu_size_id)

    if not menu_size:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu_size


@router.patch("/{menu_size_id}", response_model=MenuSize)
async def update_menu_size(
    menu_size_id: int,
    menu_size: UpdateMenuSize,
    db: AsyncSession = Depends(get_session),
):
    updated = await menussizes.update_menu_size(db, menu_size_id, menu_size)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@router.delete("/{menu_size_id}")
async def delete_menu_size(menu_size_id: int, db=Depends(get_session)):
    deleted = await menussizes.delete_menu(db, menu_size_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Deleted"}
