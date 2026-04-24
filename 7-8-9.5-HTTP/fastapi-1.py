from fastapi import FastAPI, HTTPException,Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets


app = FastAPI()
security = HTTPBasic()
USER_DB ={"admin":"pass123"}
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf-8")
    current_password_bytes = credentials.password.encode("utf-8")
    is_valid_user = credentials.username in USER_DB

    if is_valid_user:
        correct_password_byets = USER_DB[credentials.username].encode("utf-8")
        is_correct_password = secrets.compare_digest(current_password_bytes,correct_password_byets)
    else:
        is_correct_password = False
    if not( is_valid_user and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password from amrit",
            headers={"WWW-Authenticate":"Basic"}
        )
    return credentials.username

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
def get_all_tasks(username: str = Depends(authenticate)):
    """Get all the tasks"""
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int,username: str = Depends(authenticate)):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="task not found")
    return tasks[task_id]

@app.post("/tasks")
def create_task(task:Task,username: str = Depends(authenticate)):
    new_id = max(tasks.keys()) +1 if task else 1
    tasks[new_id] = task.model_dump()
    return{"message": "Task Created", "id":new_id, "data": tasks[new_id]}

@app.put("/tasks/{task_id}")
def update_task_put(task_id: int, task: Task,username: str = Depends(authenticate)):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task number {task_id} not found")
    tasks[task_id]=task.model_dump()
    return {"message":"Task fully replaced", "data": tasks[task_id]}

@app.patch("/tasks/{task_id}")
def update_task_patch(task_id: int, task_update: TaskUpdate,username: str = Depends(authenticate)):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task number {task_id} not found")
    
    stored_task_data = tasks[task_id]
    update_data = task_update.model_dump(exclude_unset=True)
    #tasks[task_id]=taskd.model_dump()
    stored_task_data.update(update_data)
    tasks[task_id] = stored_task_data
    return {"message":"Task partially replaced", "data": tasks[task_id]}

