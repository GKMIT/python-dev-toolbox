"""task router."""

import json
import logging
from typing import Annotated

import redis.asyncio as redis
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi_crud.database.connection import get_db
from fastapi_crud.models.task import Task, TaskBase, TaskRead
from fastapi_crud.services.redis_client import get_redis_client

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")  # type: ignore[misc]
async def create_task(
    task: TaskBase,
    db: Annotated[Session, Depends(get_db)],
    r: Annotated[redis.Redis, Depends(get_redis_client)],
) -> TaskRead:
    """Create a new task in the database.

    Args:
        task (TaskBase): Pydantic model containing task data to create.
        db (Session): SQLAlchemy session dependency for DB operations.
        r (redis.Redis): Redis client dependency for cache operations.

    Returns:
        TaskRead: The created task data as a Pydantic model.

    Side Effects:
        Deletes the Redis cache key 'tasks' to invalidate cached task list.

    """
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    await r.delete("tasks")
    logger.info("Task created with ID %s", db_task.id)
    validated_response: TaskRead = TaskRead.model_validate(db_task)
    return validated_response


@router.get("/")  # type: ignore[misc]
async def read_tasks(
    db: Annotated[Session, Depends(get_db)],
    r: Annotated[redis.Redis, Depends(get_redis_client)],
) -> list[TaskRead]:
    """Retrieve all tasks from cache or database.

    First checks Redis cache for stored task list.
    If cache miss, queries the database and caches results for 60 seconds.

    Args:
        db (Session): SQLAlchemy session dependency for DB operations.
        r (redis.Redis): Redis client dependency for cache operations.

    Returns:
        List[TaskRead]: List of all tasks as Pydantic models.

    """
    cached_tasks = await r.get("tasks")
    if cached_tasks:
        logger.info("Returning tasks from Redis cache")
        task_dicts = json.loads(cached_tasks)
        return [TaskRead(**task) for task in task_dicts]

    tasks = db.query(Task).all()
    task_dicts = [TaskRead.from_orm(task).dict() for task in tasks]
    await r.setex("tasks", 60, json.dumps(task_dicts))
    logger.info("Cached tasks in Redis for 60 seconds")
    return [TaskRead.from_orm(task) for task in tasks]


@router.get("/{task_id}")  # type: ignore[misc]
async def read_task(
    task_id: int,
    db: Annotated[Session, Depends(get_db)],
) -> TaskRead:
    """Retrieve a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.
        db (Session): SQLAlchemy session dependency for DB operations.

    Returns:
        TaskRead: The requested task as a Pydantic model.

    Raises:
        HTTPException: If task with given ID does not exist (404 Not Found).

    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        logger.warning("Task %s not found", task_id)
        raise HTTPException(status_code=404, detail="Task not found")
    validated_response: TaskRead = TaskRead.model_validate(task)
    return validated_response


@router.put("/{task_id}")  # type: ignore[misc]
async def update_task(
    task_id: int,
    task: TaskBase,
    db: Annotated[Session, Depends(get_db)],
    r: Annotated[redis.Redis, Depends(get_redis_client)],
) -> TaskRead:
    """Update an existing task by ID.

    Args:
        task_id (int): The ID of the task to update.
        task (TaskBase): Pydantic model containing updated task data.
        db (Session): SQLAlchemy session dependency for DB operations.
        r (redis.Redis): Redis client dependency for cache invalidation.

    Returns:
        TaskRead: The updated task as a Pydantic model.

    Raises:
        HTTPException: If task with given ID does not exist (404 Not Found).

    Side Effects:
        Deletes the Redis cache key 'tasks' to invalidate cached task list.

    """
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        logger.warning("Task %s not found for update", task_id)
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task.model_dump().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    await r.delete("tasks")
    logger.info("Task %s updated", task_id)
    validated_response: TaskRead = TaskRead.model_validate(db_task)
    return validated_response


@router.delete("/{task_id}")  # type: ignore[misc]
async def delete_task(
    task_id: int,
    db: Annotated[Session, Depends(get_db)],
    r: Annotated[redis.Redis, Depends(get_redis_client)],
) -> dict[str, str]:
    """Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to delete.
        db (Session): SQLAlchemy session dependency for DB operations.
        r (redis.Redis): Redis client dependency for cache invalidation.

    Returns:
        Dict[str, str]: A dictionary containing a success message.

    Raises:
        HTTPException: If task with given ID does not exist (404 Not Found).

    Side Effects:
        Deletes the Redis cache key 'tasks' to invalidate cached task list.

    """
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        logger.warning("Task %s not found for deletion", task_id)
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    await r.delete("tasks")
    logger.info("Task %s deleted", task_id)
    return {"detail": "Task deleted"}
