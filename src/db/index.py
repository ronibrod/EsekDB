from pymongo import MongoClient
from bson import json_util
import json

client = MongoClient('mongodb://localhost:27017/')

def get_collection(user_name, collection_name):
    db = client[user_name]
    return db[collection_name]

def bson_to_json(data):
    return json.loads(json_util.dumps(data))