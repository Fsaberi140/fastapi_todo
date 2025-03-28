from fastapi import FastAPI
from app.routes import todo

app = FastAPI()

app.include_router(todo.router, prefix="/todos", tags=["todos"])

# توضیحات
# https://chatgpt.com/c/67e2ed1a-a520-8006-9803-2e927285af57