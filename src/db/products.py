from .index import get_collection

def get_products(user_name):
    productCollection = get_collection(user_name, 'product')
    
    return list(productCollection.find({}))
