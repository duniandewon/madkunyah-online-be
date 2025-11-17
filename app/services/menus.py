from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import Menu as menu_db, ModifierGroup as modifier_group_db
from app.schemas import CreateMenu, UpdateMenu


async def get_all_menus(db: AsyncSession, skip: int, limit: int):
    query = select(menu_db)

    query = query.options(
        selectinload(menu_db.modifier_groups).selectinload(modifier_group_db.items)
    )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


async def get_menu_by_id(db: AsyncSession, menu_id: int):
    query = select(menu_db)

    query = query.options(
        selectinload(menu_db.modifier_groups).selectinload(modifier_group_db.items)
    )

    q = await db.execute(query.where(menu_db.id == menu_id))

    return q.scalars().first()


async def create_menu(db: AsyncSession, item: CreateMenu):
    menu_data = item.model_dump()
    new_menu = menu_db(**menu_data)

    db.add(new_menu)

    await db.commit()
    await db.refresh(new_menu)

    return new_menu


async def update_menu(db: AsyncSession, item_id: int, menu_update: UpdateMenu):
    stmt = (
        select(menu_db)
        .where(menu_db.id == item_id)
        .options(
            selectinload(menu_db.modifier_groups).selectinload(modifier_group_db.items)
        )
    )
    result = await db.execute(stmt)
    db_obj = result.scalar_one_or_none()

    if not db_obj:
        return None

    update_data = menu_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    await db.commit()
    await db.refresh(db_obj)

    return db_obj


async def delete_menu(db: AsyncSession, menu_id: int):
    item = await db.get(menu_db, menu_id)

    if item:
        await db.delete(item)
        await db.commit()

    return item


async def add_modifiers_to_menu(db: AsyncSession, menu_id: int, modifier_group_id: int):
    menu_obj = await db.get(
        menu_db,
        menu_id,
        options=[
            selectinload(menu_db.modifier_groups).selectinload(modifier_group_db.items)
        ],
    )
    if not menu_obj:
        return None

    group_obj = await db.get(modifier_group_db, modifier_group_id)
    if not group_obj:
        return None

    if group_obj not in menu_obj.modifier_groups:
        menu_obj.modifier_groups.append(group_obj)

    await db.commit()
    await db.refresh(menu_obj, attribute_names=["modifier_groups"])

    return menu_obj


async def remove_modifiers_from_menu(
    db: AsyncSession, menu_id: int, modifier_group_id: int
):
    menu_obj = await db.get(
        menu_db, menu_id, options=[selectinload(menu_db.modifier_groups)]
    )
    if not menu_obj:
        return None

    group_obj = await db.get(modifier_group_db, modifier_group_id)
    if not group_obj:
        return None

    try:
        menu_obj.modifier_groups.remove(group_obj)
    except ValueError:
        pass

    await db.commit()
    await db.refresh(menu_obj, attribute_names=["modifier_groups"])

    return menu_obj
