import uvicorn

from app.core.config import get_settings

settings = get_settings()


def main():
    uvicorn.run("app.app:app", host=settings.HOST, port=settings.PORT, reload=True)


if __name__ == "__main__":
    main()
