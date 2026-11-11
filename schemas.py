from pydantic import BaseModel, Field
from typing import Literal

class TaskCreate(BaseModel):

    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)
    priority: Literal["Low", "Medium", "High"]
    status: Literal["Pending", "In Progress", "Completed"]

class TaskUpdate(BaseModel):

    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, min_length=1)
    priority: Literal["Low", "Medium", "High"] | None = None
    status: Literal["Pending", "In Progress", "Completed"] | None = None