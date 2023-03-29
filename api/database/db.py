from pymongo import MongoClient
from config import MONGODB_URI, DATABASE
db = MongoClient(MONGODB_URI)[DATABASE]