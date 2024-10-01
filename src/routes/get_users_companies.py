from ..db.user import get_user
from ..db.company import get_companies

def handle_get_users_companies(request):
    user_name = request['user_name']
    
    userQuery = { 'user_name': user_name }
    userProjection = { 'companies': True }
    user_data = get_user(userQuery, userProjection)
    
    companyQuery = { '_id': { '$in': user_data['companies'] } }
    companyProjection = { '_id': True, 'official_name': True, 'typical_name': True }
    list_of_users_companies = get_companies(companyQuery, companyProjection)
    print(list_of_users_companies)

    return list_of_users_companies
