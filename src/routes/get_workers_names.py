from ..db.workers import get_workers

def handle_get_workers_names(request):
    user_name = request['user_name']
    
    query = {}
    projection = { 
        '_id': True,
        'user_name': True,
        'name': True,
        'full_name': True,
    }
    list_of_workers_names = get_workers(user_name, query, projection)

    return list_of_workers_names
