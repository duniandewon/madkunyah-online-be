from fastapi import APIRouter

from app.routes.v1 import menus, modifier_group, modifier_item

router = APIRouter(prefix="/api/v1")

router.include_router(menus.router, prefix="/menus", tags=["menus"])

router.include_router(
    modifier_group.router, prefix="/modifier_group", tags=["modifier_group"]
)

router.include_router(
    modifier_item.router, prefix="/modifier_item", tags=["modifier_item"]
)
