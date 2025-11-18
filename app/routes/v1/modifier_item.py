from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session

from app.schemas import ModifierItem, CreateModifierItem, UpdateModifierItem

from app.services import modifier_item

router = APIRouter()


@router.post("/", response_model=ModifierItem)
async def create_modifier_item(
    modifier_item_data: CreateModifierItem, db: AsyncSession = Depends(get_session)
):
    new_modifier_item = await modifier_item.create_modifier_item(db, modifier_item_data)

    if not new_modifier_item:
        raise HTTPException(status_code=400, detail="Invalid modifier group id")

    return new_modifier_item


@router.patch("/{modifier_item_id}", response_model=ModifierItem)
async def create_modifier_item(
    modifier_item_id: int,
    modifier_item_data: UpdateModifierItem,
    db: AsyncSession = Depends(get_session),
):
    updated = await modifier_item.update_modifier_item(
        db, modifier_item_id, modifier_item_data
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Modifier item not found")

    return updated


@router.delete("/{modifier_item_id}", response_model=ModifierItem)
async def create_modifier_item(
    modifier_item_id: int,
    db: AsyncSession = Depends(get_session),
):
    deleted = await modifier_item.delete_modifier_item(db, modifier_item_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Modifier item not found")

    return deleted
