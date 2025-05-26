"""Redis client."""

import os

import redis.asyncio as redis
from fastapi import Request

# Redis configuration
REDIS_URL = os.getenv("REDIS_URL")
redis_pool = redis.ConnectionPool.from_url(REDIS_URL)


async def create_redis_client() -> redis.Redis:
    """Create a Redis client."""
    return redis.Redis(connection_pool=redis_pool)


async def close_redis_client(client: redis.Redis) -> None:
    """Close Redis client."""
    await client.close()


def get_redis_client(request: Request) -> redis.Redis:
    """Retrieve Redis client from app state."""
    return request.app.state.redis
