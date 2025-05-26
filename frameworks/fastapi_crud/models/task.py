"""Tasks model."""

from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String

from fastapi_crud.database.connection import Base


class Task(Base):
    """SQLAlchemy model for the tasks table,representing a task in the CRUD application.

    Attributes:
        id (int): Unique identifier for the task, auto-incremented primary key.
        title (str): Brief title of the task, indexed for faster queries.
        description (str): Detailed description of the task.
        completed (bool): Indicates whether the task is completed, defaults to False.

    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)


class TaskBase(BaseModel):  # type: ignore[misc]
    """Pydantic model for Task."""

    title: str
    description: str
    completed: bool = False
    model_config = {"from_attributes": True}


class TaskRead(TaskBase):
    """Pydantic model for task output, includes the ID."""

    id: int
    model_config = {"from_attributes": True}

    class Config:
        """ORM config."""

        orm_mode = True
