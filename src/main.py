import uvicorn
from fastapi import FastAPI

from api import router as api_router
from core.config import settings

app = FastAPI(prefix="/app")

app.include_router(api_router, prefix=settings.api.prefix)
