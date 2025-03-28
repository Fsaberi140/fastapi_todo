from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()  # بارگذاری متغیرهای محیطی از فایل .env

MONGO_URI = os.getenv("MONGO_URI")  # خواندن URL دیتابیس از .env

# ایجاد کلاینت MongoDB
client = AsyncIOMotorClient(MONGO_URI)
database = client.todo_database
todo_collection = database.get_collection("todos")

# توضیحات
# https://chatgpt.com/c/67e2ed1a-a520-8006-9803-2e927285af57