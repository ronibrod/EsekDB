from .index import get_collection

def create_company(query):
    companyCollection = get_collection('users', 'companies')
    
    result = companyCollection.insert_one(query)
    return { '_id': str(result.inserted_id) }

def get_companies(query, projection={}):
    companyCollection = get_collection('users', 'companies')
    
    return list(companyCollection.find(query, projection))
