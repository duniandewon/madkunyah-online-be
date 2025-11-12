from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from typing import TypeVar, Any

from app.models import Menu, MenuSize, Option
from app.schemas.menus import CreateMenu, UpdateMenu

RelatedModel = TypeVar("RelatedModel", bound=Any)


async def _update_menu_relationship(
    db: AsyncSession,
    menu_id: int,
    related_id: int,
    relationship_attr: str,
    related_model: RelatedModel,
    action: str,
):
    menu_obj = await db.get(
        Menu, menu_id, options=[selectinload(getattr(Menu, relationship_attr))]
    )
    related_obj = await db.get(related_model, related_id)

    if not menu_obj or not related_obj:
        return None

    collection = getattr(menu_obj, relationship_attr)

    if action == "add":
        if related_obj not in collection:
            collection.append(related_obj)
    elif action == "remove":
        try:
            collection.remove(related_obj)
        except ValueError:
            pass
    else:
        raise ValueError("Invalid action. Must be 'add' or 'remove'.")

    await db.commit()
    await db.refresh(menu_obj)
    return menu_obj


async def create_menu(db: AsyncSession, item: CreateMenu) -> Menu:
    menu_data = item.model_dump(exclude={"size_ids", "option_ids"})

    new_menu = Menu(**menu_data)

    db.add(new_menu)
    await db.commit()

    await db.refresh(
        new_menu,
        attribute_names=[
            "sizes",
            "options",
        ],
        with_for_update=False,
    )

    return new_menu


async def get_all_menus(db: AsyncSession, skip: int, limit: int):
    query = select(Menu)

    query = query.options(selectinload(Menu.sizes), selectinload(Menu.options))

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


async def get_menu_by_id(db: AsyncSession, menu_id: int):
    q = await db.execute(select(Menu).where(Menu.id == menu_id))
    return q.scalars().first()


async def update_menu(db: AsyncSession, item_id: int, menu_update: UpdateMenu):
    stmt = (
        select(Menu)
        .where(Menu.id == item_id)
        .options(selectinload(Menu.sizes), selectinload(Menu.options))
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
    item = await db.get(Menu, menu_id)

    if item:
        await db.delete(item)
        await db.commit()

    return item


async def add_size_to_menu(db: AsyncSession, menu_id: int, size_id: int):
    return await _update_menu_relationship(
        db,
        menu_id,
        size_id,
        relationship_attr="sizes",
        related_model=MenuSize,
        action="add",
    )


async def remove_size_from_menu(db: AsyncSession, menu_id: int, size_id: int):
    return await _update_menu_relationship(
        db,
        menu_id,
        size_id,
        relationship_attr="sizes",
        related_model=MenuSize,
        action="remove",
    )


async def add_option_to_menu(db: AsyncSession, menu_id: int, option_id: int):
    return await _update_menu_relationship(
        db,
        menu_id,
        option_id,
        relationship_attr="options",
        related_model=Option,
        action="add",
    )


async def remove_option_from_menu(db: AsyncSession, menu_id: int, option_id: int):
    return await _update_menu_relationship(
        db,
        menu_id,
        option_id,
        relationship_attr="options",
        related_model=Option,
        action="remove",
    )
