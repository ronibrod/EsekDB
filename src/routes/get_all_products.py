from ..db.products import get_products

def handle_get_all_products(request):
    user_name = request.user_name
    
    list_of_products = get_products(user_name)
    
    for product in list_of_products:
        if '_id' in product:
            product['_id'] = str(product['_id'])

    return list_of_products
