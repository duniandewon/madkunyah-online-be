from fastapi import APIRouter

from app.routes.v1 import menus

router = APIRouter(prefix="/api/v1")

router.include_router(menus.router, prefix="/menus", tags=["menus"])
