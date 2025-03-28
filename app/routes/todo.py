# app/routes/todo.py

from fastapi import APIRouter
from fastapi import HTTPException
from bson import ObjectId

from app.core.database import todo_collection
from app.schemas.todo import TodoCreate, TodoResponse
from app.schemas.todo import TodoBase

router = APIRouter()

# create
@router.post("/", response_model=TodoResponse)
async def create_todo(todo: TodoCreate):
    new_todo = todo.model_dump()
    result_create = await todo_collection.insert_one(new_todo)
    created_todo = await todo_collection.find_one({"_id": result_create.inserted_id})
    return {**created_todo, "id": str(created_todo["_id"])}

# توضیحات
# https://chatgpt.com/c/67e2ed1a-a520-8006-9803-2e927285af57




# read
# خواندن همه تسک ها
@router.get('/', response_model=TodoResponse)
async def get_all_todos():
    todos=[]
    async for todo in todo_collection.find():
        todos.append(TodoResponse(**todo, id=str(todo["_id"])))
    return todos


# خواندن یک تسک خاص
@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo_by_id(todo_id: str):
    # بررسی معتبر بودن ObjectId
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid Todo ID")

    todo = await todo_collection.find_one({"_id": ObjectId(todo_id)})
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return TodoResponse(**todo, id=str(todo["_id"]))

# توضیحات
# https://chatgpt.com/c/67e721a2-b2cc-8006-9b9c-a128a6062ac2




# update
@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: str, updated_todo: TodoBase):

    # چک کردن آیا تسک با ID موردنظر وجود دارد یا نه
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid Todo ID")

    # بروزرسانی تسک در دیتابیس
    result_update = await todo_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": updated_todo.model_dump(exclude_unset=True)}
    )

    if result_update.modified_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")

    # برگرداندن تسک بروزرسانی‌شده
    updated_todo = await todo_collection.find_one({"_id": ObjectId(todo_id)})
    return {**updated_todo, "id": str(updated_todo["_id"])}

# توضیحات
# https://chatgpt.com/c/67e30731-09c4-8006-9deb-8b4de7ac0633



# delete
@router.delete("/{todo_id}", response_model=dict)
async def delete_todo(todo_id: str):
    # چک کردن آیا ID معتبر است یا خیر
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid Todo ID")

    # حذف تسک از دیتابیس
    result_delete = await todo_collection.delete_one({"_id": ObjectId(todo_id)})

    if result_delete.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": f"Todo with ID {todo_id} deleted successfully."}