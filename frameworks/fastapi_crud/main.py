"""main file."""

import json
import logging
import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_crud.database.connection import init_db
from fastapi_crud.routers.tasks import router as task_router
from fastapi_crud.services.redis_client import close_redis_client, create_redis_client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Lifespan for the app."""
    logger.info("Starting up application...")
    init_db()
    app.state.redis = await create_redis_client()
    logger.info("Database and Redis initialized.")
    yield
    logger.info("Shutting down application...")
    await close_redis_client(app.state.redis)
    logger.info("Redis connection closed.")


app = FastAPI(lifespan=lifespan)

origins = json.loads(os.environ.get("ALLOWED_ORIGINS", '["http://localhost:4200"]'))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)


@app.get("/health") # type: ignore[misc]
async def health_check() -> dict[str, str]:
    """Health check."""
    return {"status": "healthy"}
