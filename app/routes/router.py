from fastapi import APIRouter

from app.routes.v1 import menus, menusizes, options

router = APIRouter(prefix="/api/v1")

router.include_router(menus.router, prefix="/menus", tags=["menus"])

router.include_router(menusizes.router, prefix="/menu-size", tags=["menu-sizes"])

router.include_router(options.router, prefix="/options", tags=["options"])
