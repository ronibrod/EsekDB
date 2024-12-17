from pymongo import MongoClient
from bson import json_util
import json

uri = "mongodb+srv://ronibrod:z1wpjxT5KaDvMGHg@esekprocluster.gdad5.mongodb.net/?retryWrites=true&w=majority&appName=EsekProCluster&tls=true&tlsInsecure=true"
# client = MongoClient('mongodb+srv://<username>:<password>@esekprocluster.xxxxx.mongodb.net/<dbname>?retryWrites=true&w=majority')

# client = MongoClient('localhost', 27017)

def get_collection(user_name, collection_name):
    try:
        client = MongoClient(uri)
        db = client.test
        print("Connected to MongoDB!")
        
        db = client[user_name]
        collection = db[collection_name]
        
        return collection
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")

def bson_to_json(data):
    return json.loads(json_util.dumps(data))
