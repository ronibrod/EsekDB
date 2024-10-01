import bcrypt
from datetime import datetime
from ..db.user import create_user, get_user

def handle_post_signup(request):
    user_name = request.get('user_name')
    password = request.get('password')
    
    if not user_name or not password:
        return { "error": "Username and password are required" }, 400
    
    created_at = datetime.now()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_id = f"{user_name}_{created_at.strftime('%Y-%m-%d_%H-%M-%S')}"
    
    query = {
        '_id': user_id,
        'user_name': user_name,
        'password': hashed_password,
        'created_at': created_at,
        'companies': [],
    }
    
    try:
        user_data = create_user(query)
        
        if not user_data:
            return {"error": "Failed to create user"}, 500
        
        return {'user_data': user_data}, 200
        
    except Exception as e:
        return {"error": str(e)}, 500

def handle_post_login(request):
    user_name = request.get('user_name')
    password = request.get('password')
    
    if not user_name or not password:
        return { "error": "Username and password are required" }, 400

    try:
        user_data = get_user({ 'user_name': user_name })
        if not user_data:
            return {"error": "Invalid username or password"}, 401
        
        stored_hashed_password = user_data['password']
        if not bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
            return {"error": "Invalid username or password"}, 401
        
        return {'user_data': { '_id': user_data['_id'] }}, 200
    
    except Exception as e:
        return {"error": str(e)}, 500
