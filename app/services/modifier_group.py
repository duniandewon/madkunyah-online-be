from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import ModifierGroup as modifier_group_db
from app.schemas import CreateModifierGroup, UpdateModifierGroup


async def get_all_modifier_group(db: AsyncSession, skip: int, limit: int):
    query = select(modifier_group_db)

    query = query.options(selectinload(modifier_group_db.items))

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


async def get_modifier_group_by_id(db: AsyncSession, item_id: int):
    query = select(modifier_group_db)

    query = query.options(selectinload(modifier_group_db.items))

    result = await db.execute(query.where(modifier_group_db.id == item_id))

    return result.scalars().first()


async def create_modifier_group(db: AsyncSession, modifier_group: CreateModifierGroup):
    new_modifier_group = modifier_group_db(**modifier_group.model_dump())

    db.add(new_modifier_group)

    await db.commit()
    await db.refresh(new_modifier_group)

    return new_modifier_group


async def update_modifier_group(
    db: AsyncSession, item_id: int, modifier_group: UpdateModifierGroup
):
    stmt = (
        select(modifier_group_db)
        .where(modifier_group_db.id == item_id)
        .options(selectinload(modifier_group_db.items))
    )

    result = await db.execute(stmt)
    db_obj = result.scalar_one_or_none()

    if not db_obj:
        return None

    update_data = modifier_group.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    await db.commit()
    await db.refresh(db_obj)

    return db_obj


async def delete_modifier_group(db: AsyncSession, item_id: int):
    item = await db.get(modifier_group_db, item_id)

    if item:
        await db.delete(item)
        await db.commit()

    return item
