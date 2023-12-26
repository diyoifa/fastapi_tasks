from fastapi import APIRouter, Depends, status
from ..dependencies import auth_user
from ..schemas.task import task_schema
from ..models.task import  Task
from ..config.db import client
from bson.objectid import ObjectId


router = APIRouter(
    prefix="/task",
    tags=["Task"],
    responses={404: {"description": "Not found"}},
)

@router.get('/', status_code=status.HTTP_200_OK)
async def all_tasks(user = Depends(auth_user)):
    # print('user: ', user)
    return user.get("tasks")

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_task(task: Task, user = Depends(auth_user)):

    task_dict = dict(task)
    del task_dict["id"]

    id = client.tasks.insert_one(task_dict)

    new_task = task_schema(client.tasks.find_one({"_id": id.inserted_id}))
    user = client.users.find_one_and_update(
        {"email": user.get("email")}, 
        {"$push": {"tasks": new_task}}
    )
    
    return new_task


@router.put('/{task_id}', status_code=status.HTTP_200_OK)
async def update_task(task_id: str, task: Task, user = Depends(auth_user)):
    
    task_dict = dict(task)
    del task_dict["id"]
    client.tasks.find_one_and_update({"_id": ObjectId(task_id)}, {"$set": task_dict})

    updated_task = task_schema(client.tasks.find_one({"_id": ObjectId(task_id)}))

    client.users.update_one(
        {"email": user.get("email"), "tasks.id": task_id},
        {"$set": {"tasks.$": updated_task}}
    )
    return updated_task

@router.delete('/{task_id}', status_code=status.HTTP_200_OK)
async def delete_task(task_id: str, user = Depends(auth_user)):

    client.tasks.find_one_and_delete({"_id": ObjectId(task_id)})
    client.users.update_one(
        {"email": user.get("email")},
        {"$pull": {"tasks": {"id": task_id}}}
    )
    return {"message": "Task deleted successfully"}
