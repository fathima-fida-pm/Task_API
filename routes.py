from fastapi import APIRouter, HTTPException, status

from schemas import TaskCreate, TaskUpdate

import crud


router = APIRouter()


# CREATE TASK
@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_new_task(task: TaskCreate):

    return crud.create_task(task)


# GET ALL TASKS
@router.get("/tasks")
def get_tasks(
    status: str | None = None,
    priority: str | None = None
):

    return crud.get_all_tasks(status, priority)


# GET TASK BY ID
@router.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):

    existing_task = crud.get_task_by_id(task_id)

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return existing_task


# UPDATE TASK
@router.put("/tasks/{task_id}")
def update_existing_task(task_id: int, task: TaskUpdate):

    existing_task = crud.get_task_by_id(task_id)

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    updated_data = task.model_dump(exclude_unset=True)

    if not updated_data:
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    crud.update_task(task_id, updated_data)

    return crud.get_task_by_id(task_id)

# DELETE TASK
@router.delete("/tasks/{task_id}")
def delete_existing_task(task_id: int):

    deleted = crud.delete_task(task_id)

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}