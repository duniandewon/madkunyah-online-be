from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ModifierItem as modifier_item_db
from app.schemas import CreateModifierItem, UpdateModifierItem


async def get_all_modifier_item(db: AsyncSession, skip: int, limit: int):
    query = select(modifier_item_db)

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


async def get_modifier_item_by_id(db: AsyncSession, item_id: int):
    query = select(modifier_item_db)

    result = await db.execute(query.where(modifier_item_db.id == item_id))

    return result.scalars().first()


async def create_modifier_item(db: AsyncSession, modifier_group: CreateModifierItem):
    new_modifier_item = modifier_item_db(**modifier_group.model_dump())

    db.add(new_modifier_item)

    await db.commit()
    await db.refresh(new_modifier_item)

    return new_modifier_item


async def update_modifier_item(
    db: AsyncSession, item_id: int, modifier_group: UpdateModifierItem
):
    stmt = select(modifier_item_db).where(modifier_item_db.id == item_id)

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


async def delete_modifier_item(db: AsyncSession, item_id: int):
    item = await db.get(modifier_item_db, item_id)

    if item:
        await db.delete(item)
        await db.commit()

    return item
