from pymongo import mongo_client

import pymongo

from app.config import settings

client = mongo_client.MongoClient(
    settings.DATABASE_URL, serverSelectionTimeoutMS=5000
)

try:
    conn = client.server_info()
    print(f'Connected to mongoDB {conn.get("version")}')
except Exception:
    print("Unable to connect to mongo server.")

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users

User.create_index([("email", pymongo.ASCENDING)], unique=True)
