from .index import get_collection

def get_sales(user_name, query):
    productCollection = get_collection(user_name, 'sale')
    
    return list(productCollection.find(query))
