import bcrypt
from datetime import datetime
from ..db.user import get_user, update_user
from ..db.workers import create_worker
from ..db.company import create_company

def handle_post_create_company(request):
    user_creator_id = request.get('user_id')
    user_name = request.get('user_name')
    password = request.get('companyPassword')
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    created_at = datetime.now()
    company_id = f"{user_name}_{created_at.strftime('%Y-%m-%d_%H-%M-%S')}"
    official_name = request.get('companyOfficialName')
    
    query = {
        '_id': company_id,
        'user_creator_name': user_name,
        'user_creator_id': user_creator_id,
        'official_name': official_name,
        'typical_name': request.get('companyTypicalName'),
        'password': hashed_password,
        'created_at': created_at,
    }

    try:
        user_data = get_user({ '_id': user_creator_id, 'user_name': user_name })
        if not user_data:
            return {"error": "Failed to create company, user data invalid"}, 500
        
        company_data = create_company(query)
        if not company_data:
            return {"error": "Failed to create company, company data invalid"}, 500
        
        update_user({ '_id': user_creator_id }, { '$push': { 'companies': company_id } })
        worker_data = {
            '_id': user_creator_id,
            'user_name': user_name,
            'created_at': created_at,
            'user_level': 'businessOwner',
        }
        create_worker(official_name , worker_data)
        
        return {'company_data': company_data}, 200
        
    except Exception as e:
        return {"error": str(e)}, 500
