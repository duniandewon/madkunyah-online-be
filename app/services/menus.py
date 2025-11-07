from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.menus import Menu
from app.schemas.menus import CreateMenu, UpdateMenu


async def create_menu(db: AsyncSession, item: CreateMenu) -> Menu:
    entity = Menu(**item.model_dump())
    db.add(entity)
    await db.commit()
    await db.refresh(entity)
    return entity


async def get_all_menus(db: AsyncSession, skip: int, limit: int):
    query = select(Menu)

    result = await db.execute(query.offset(skip).limit(limit))

    return result.scalars().all()


async def get_menu_by_id(db: AsyncSession, menu_id: int):
    q = await db.execute(select(Menu).where(Menu.id == menu_id))
    return q.scalars().first()


async def update_menu(db: AsyncSession, item_id: int, menu_update: UpdateMenu):
    db_obj = await db.get(Menu, item_id)
    if not db_obj:
        return None

    update_data = menu_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def delete_menu(db: AsyncSession, menu_id: int):
    item = await db.get(Menu, menu_id)

    if item:
        await db.delete(item)
        await db.commit()

    return item
