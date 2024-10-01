from datetime import datetime
from ..db.sales import get_sales

def handle_get_sales(request):
    user_name = request.user_name
    query = {
        'date': {
            '$gte': datetime.strptime(request['startTime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
            '$lte': datetime.strptime(request['endTime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
        },
    }
    
    if 'products' in request:
        query['product'] = {'$in': request['products']}

    if 'categories' in request:
        query['category'] = {'$in': request['categories']}

    list_of_sales = get_sales(user_name, query)
    for sale in list_of_sales:
        if '_id' in sale:
            sale['_id'] = str(sale['_id'])

    return list_of_sales
