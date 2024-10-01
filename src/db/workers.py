from .index import get_collection

def create_worker(company_name, query):
    workerCollection = get_collection(company_name, 'worker')
    
    result = workerCollection.insert_one(query)
    return { '_id': str(result.inserted_id) }

def get_workers(company_name, query, projection={}):
    workerCollection = get_collection(company_name, 'worker')
    
    return list(workerCollection.find(query, projection))

