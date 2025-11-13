from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import Option, CreateOption, UpdateOption

from app.core.db import get_session

from app.services import options

router = APIRouter()


@router.get("/", response_model=List[Option])
async def get_all_option(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)
):
    return await options.get_all_options(db, skip, limit)


@router.get("/{option_id}", response_model=Option)
async def get_option_by_id(option_id: int, db: AsyncSession = Depends(get_session)):
    return await options.get_option_by_id(db, option_id)


@router.post("/", response_model=Option)
async def create_option(option: CreateOption, db: AsyncSession = Depends(get_session)):
    return await options.create_option(db, option)


@router.patch("/{option_id}", response_model=Option)
async def update_option(
    option_id: int,
    option: UpdateOption,
    db: AsyncSession = Depends(get_session),
):
    updated = await options.update_option(db, option_id, option)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@router.delete("/{option_id}")
async def delete_option(option_id: int, db=Depends(get_session)):
    deleted = await options.delete_option(db, option_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Deleted"}
