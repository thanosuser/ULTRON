import asyncio
import sys
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from ULTRON import MONGO_DB_URI


MONGO_PORT = "27017"
MONGO_DB_URI = "mongodb+srv://lucyx:rishabh123classmate@cluster0.hx2qi.mongodb.net/lucyx?retryWrites=true&w=majority"
MONGO_DB = "lucyx"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, 27017)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, 27017)
db = motor[MONGO_DB]
db = client["lucyx"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
