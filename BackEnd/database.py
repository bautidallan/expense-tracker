import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_TLS = os.getenv("MONGO_TLS", "false").lower() == "true"

if MONGO_TLS:
    client = AsyncIOMotorClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
else:
    client = AsyncIOMotorClient(MONGO_URI)

db = client.expense_tracker