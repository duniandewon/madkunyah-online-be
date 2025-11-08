from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router
from .core.config import get_settings

settings = get_settings()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router)
