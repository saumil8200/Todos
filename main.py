from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "name": "Task #1"},
    {"id": 2, "name": "Task #2"},
]

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.post("/tasks")
async def create_task(task):
    new_task = {"id": len(tasks) + 1, "name": task}
    tasks.append(new_task)
    return new_task

@app.delete("/tasks")
async def delete_task(task_id: int):
    task_deleted = None
    for task in tasks:
        if task["id"] == task_id:
            task_deleted = tasks.pop(tasks.index(task))
            break
    if task_deleted:
            return {"message": f"Task {task_id} deleted successfully"}
    else:
        return {"message": f"No task found with ID {task_id}"}