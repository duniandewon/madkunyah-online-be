from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session

from app.services import modifier_group as modifier_group_service

from app.schemas import (
    ModifierGroup,
    ModifierGroupSimple,
    CreateModifierGroup,
    UpdateModifierGroup,
)

router = APIRouter()


@router.get("/", response_model=List[ModifierGroupSimple])
async def get_all_modifier_group(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)
):
    return await modifier_group_service.get_all_modifier_group(db, skip, limit)


@router.get("/{modifier_group_id}", response_model=ModifierGroup)
async def get_modifier_group_by_id(
    modifier_group_id: int, db: AsyncSession = Depends(get_session)
):
    res = await modifier_group_service.get_modifier_group_by_id(db, modifier_group_id)

    if not res:
        raise HTTPException(status_code=404, detail="Modifier group not found")

    return res


@router.post("/", response_model=ModifierGroup)
async def create_modifier_group(
    modifier_group_data: CreateModifierGroup, db: AsyncSession = Depends(get_session)
):
    return await modifier_group_service.create_modifier_group(db, modifier_group_data)


@router.patch("/{modifier_group_id}", response_model=ModifierGroup)
async def update_modifier_group(
    modifier_group_id: int,
    modifier_group_data: UpdateModifierGroup,
    db: AsyncSession = Depends(get_session),
):
    updated = await modifier_group_service.update_modifier_group(
        db, modifier_group_id, modifier_group_data
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Modifier group not found")

    return updated


@router.delete("/{modifier_group_id}", response_model=ModifierGroup)
async def remove_modifier_group(
    modifier_group_id: int,
    db: AsyncSession = Depends(get_session),
):
    deleted = await modifier_group_service.delete_modifier_group(db, modifier_group_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Modifier group not found")

    return deleted
