from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Madkunyah Online Ordering")

app.include_router(router.router)
