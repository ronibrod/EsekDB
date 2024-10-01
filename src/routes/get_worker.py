from ..db.workers import get_workers

def handle_get_worker(request):
    user_name = request['user_name']
    query = { '_id': request['worker_id'] }

    [worker_data] = get_workers(user_name, query)

    return worker_data

def handle_get_worker_level(request):
    company_name = request['company_name']
    query = { '_id': request['worker_id'] }
    projection = { 'user_level': True }

    worker_data = get_workers(company_name, query, projection)

    return worker_data[0]
