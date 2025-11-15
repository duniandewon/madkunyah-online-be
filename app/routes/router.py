from fastapi import APIRouter

from app.routes.v1 import menus, modifier_group

router = APIRouter(prefix="/api/v1")

router.include_router(menus.router, prefix="/menus", tags=["menus"])

router.include_router(
    modifier_group.router, prefix="/modifier_group", tags=["modifier_group"]
)
