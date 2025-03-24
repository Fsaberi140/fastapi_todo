# app/routes/todo.py

from fastapi import APIRouter
from app.schemas.todo import TodoCreate, TodoResponse
from app.core.database import todo_collection
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=TodoResponse)
async def create_todo(todo: TodoCreate):
    new_todo = todo.model_dump()
    result = await todo_collection.insert_one(new_todo)
    created_todo = await todo_collection.find_one({"_id": result.inserted_id})
    return {**created_todo, "id": str(created_todo["_id"])}

# آموزش:
# https://chatgpt.com/c/67ded71b-87dc-8006-9597-b247bc4c4627