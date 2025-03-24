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
