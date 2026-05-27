import os
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb+srv://bautidallan2000_db_user:test@cluster0.wp9sbv0.mongodb.net/?appName=Cluster0")
db = client.expense_app # one database

