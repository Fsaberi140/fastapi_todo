# app/schemas/todo.py

from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
# TodoBase: مدل اصلی که شامل تمام فیلدهای To-Do Item است.

class TodoCreate(TodoBase):
    pass  # این کلاس برای ساخت تسک جدید است

class TodoResponse(TodoBase):
    id: str  # این کلاس پاسخ API را با id برمی‌گرداند


# توضیحات
# https://chatgpt.com/c/67e2ed1a-a520-8006-9803-2e927285af57