from pymongo import MongoClient
from  ..utils.dot_env import MONGO_DB_URI

client = MongoClient(MONGO_DB_URI).test
