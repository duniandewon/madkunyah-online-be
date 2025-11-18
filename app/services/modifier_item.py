from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ModifierItem as modifier_item_db
from app.schemas import CreateModifierItem, UpdateModifierItem

from app.services.modifier_group import get_modifier_group_by_id


async def get_all_modifier_item(db: AsyncSession, skip: int, limit: int):
    query = select(modifier_item_db)

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


async def get_modifier_item_by_id(db: AsyncSession, item_id: int):
    query = select(modifier_item_db)

    result = await db.execute(query.where(modifier_item_db.id == item_id))

    return result.scalars().first()


async def create_modifier_item(
    db: AsyncSession, modifier_item_data: CreateModifierItem
):

    modifier_group = await get_modifier_group_by_id(
        db, modifier_item_data.group_id
    )

    if not modifier_group:
        return None

    print(f"I pass here: modifier group exist {modifier_group.id}")

    new_modifier_item = modifier_item_db(**modifier_item_data.model_dump())

    db.add(new_modifier_item)

    await db.commit()
    await db.refresh(new_modifier_item)

    return new_modifier_item


async def update_modifier_item(
    db: AsyncSession, item_id: int, modifier_item_data: UpdateModifierItem
):
    stmt = select(modifier_item_db).where(modifier_item_db.id == item_id)

    result = await db.execute(stmt)
    db_obj = result.scalar_one_or_none()

    if not db_obj:
        return None

    update_data = modifier_item_data.model_dump(exclude_unset=True)

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
