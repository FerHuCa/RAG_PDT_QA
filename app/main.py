from fastapi import FastAPI

from app.api.routes import router, storage
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.on_event("startup")
def on_startup() -> None:
    storage.init_db()


app.include_router(router)
