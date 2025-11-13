from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.menusizes import MenuSize
from app.schemas.menusizes import CreateMenuSize, UpdateMenuSize


async def get_all_menu_size(db: AsyncSession, skip: int, limit: int):
    query = select(MenuSize)

    result = await db.execute(query.offset(skip).limit(limit))

    return result.scalars().all()


async def create_menu_size(db: AsyncSession, menu_size: CreateMenuSize) -> MenuSize:
    entity = MenuSize(**menu_size.model_dump())

    db.add(entity)
    await db.commit()
    await db.refresh(entity)
    return entity


async def get_menu_size_by_id(db: AsyncSession, menu_size_id: int) -> MenuSize | None:
    q = await db.execute(select(MenuSize).where(MenuSize.id == menu_size_id))
    return q.scalars().first()


async def update_menu_size(
    db: AsyncSession, menu_size_id: int, menu_size_update: UpdateMenuSize
) -> MenuSize | None:
    db_obj = await db.get(MenuSize, menu_size_id)

    if not db_obj:
        return None

    update_data = menu_size_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def delete_menu_size(db: AsyncSession, menu_size_id: int):
    item = await db.get(MenuSize, menu_size_id)

    if item:
        await db.delete(item)
        await db.commit()

    return item
