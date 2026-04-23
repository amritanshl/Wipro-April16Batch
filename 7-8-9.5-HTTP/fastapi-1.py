from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
tasks = {
    1: {"item": "first item", "completed": True},
    2: {"item": "second item", "completed": False}
}

class Task(BaseModel):
    item: str
    completed: bool

class TaskUpdate(BaseModel):
    item: Optional[str] = None
    completed: Optional[bool] = None

@app.get("/tasks")
def get_all_tasks():
    """Get all the tasks"""
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="task not found")
    return tasks[task_id]