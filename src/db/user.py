from .index import get_collection

def create_user(query):
    userCollection = get_collection('users', 'user')
    
    result = userCollection.insert_one(query)
    return { '_id': str(result.inserted_id) }

def get_user(query, projection={}):
    userCollection = get_collection('users', 'user')
    
    return dict(userCollection.find_one(query, projection))

def update_user(query, update_query):
    userCollection = get_collection('users', 'user')

    userCollection.update_one(query, update_query)
