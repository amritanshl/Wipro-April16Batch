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

@app.post("/tasks")
def create_task(task:Task):
    new_id = max(tasks.keys()) +1 if task else 1
    tasks[new_id] = task.model_dump()
    return{"message": "Task Created", "id":new_id, "data": tasks[new_id]}

@app.put("/tasks/{task_id}")
def update_task_put(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task number {task_id} not found")
    tasks[task_id]=task.model_dump()
    return {"message":"Task fully replaced", "data": tasks[task_id]}

@app.patch("/tasks/{task_id}")
def update_task_patch(task_id: int, task_update: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task number {task_id} not found")
    
    stored_task_data = tasks[task_id]
    update_data = task_update.model_dump(exclude_unset=True)
    #tasks[task_id]=taskd.model_dump()
    stored_task_data.update(update_data)
    tasks[task_id] = stored_task_data
    return {"message":"Task partially replaced", "data": tasks[task_id]}

