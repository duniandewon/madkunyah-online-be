from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Option
from app.schemas import CreateOption, UpdateOption


async def get_all_options(db: AsyncSession, skip: int, limit: int):
    query = select(Option)

    result = await db.execute(query.offset(skip).limit(limit))

    return result.scalars().all()


async def get_option_by_id(db: AsyncSession, option_id: int):
    q = await db.execute(select(Option).where(Option.id == option_id))
    return q.scalars().first()


async def create_option(db: AsyncSession, option: CreateOption):
    entity = Option(**option.model_dump())

    db.add(entity)
    await db.commit()
    await db.refresh(entity)
    return entity


async def update_option(db: AsyncSession, option: UpdateOption, option_id: int):
    db_obj = await db.get(Option, option_id)

    if not db_obj:
        return None

    update_data = option.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def delete_option(db: AsyncSession, option_id: int):
    item = await db.get(Option, option_id)

    if item:
        await db.delete(item)
        await db.commit()

    return item
