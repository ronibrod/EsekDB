import json
from flask import Blueprint, jsonify, request
from .get_sales import handle_get_sales
from .get_all_products import handle_get_all_products
from .get_worker import handle_get_worker, handle_get_worker_level
from .get_workers_names import handle_get_workers_names
from .post_log import handle_post_login, handle_post_signup
from .post_create_company import handle_post_create_company
from .get_users_companies import handle_get_users_companies

routes = Blueprint('routes', __name__)
  
@routes.route('/getSales', methods=['GET'])
def get_sales():
    request_data = json.loads(request.args.to_dict()['query'])
    response = handle_get_sales(request_data)
    return jsonify(response)

@routes.route('/getAllProducts', methods=['GET'])
def get_all_products():
    request_data = json.loads(request.args.to_dict()['query'])
    response = handle_get_all_products(request_data)
    return jsonify(response)

@routes.route('/getWorker', methods=['GET'])
def get_worker():
    request_data = json.loads(request.args.to_dict()['query'])
    response = handle_get_worker(request_data)
    return jsonify(response)

@routes.route('/getWorkerLevel', methods=['GET'])
def get_worker_level():
    request_data = json.loads(request.args.to_dict()['query'])
    response = handle_get_worker_level(request_data)
    return jsonify(response)

@routes.route('/getWorkersNames', methods=['GET'])
def get_workers_names():
    request_data = json.loads(request.args.to_dict()['query'])
    response = handle_get_workers_names(request_data)
    return jsonify(response)

@routes.route('/signup', methods=['POST'])
def post_signup():
    request_data = request.get_json()
    response, status_code = handle_post_signup(request_data)
    return jsonify(response), status_code

@routes.route('/login', methods=['POST'])
def post_login():
    request_data = request.get_json()
    response, status_code = handle_post_login(request_data)
    return jsonify(response), status_code

@routes.route('/createCompany', methods=['POST'])
def post_create_company():
    request_data = request.get_json()
    response, status_code = handle_post_create_company(request_data)
    return jsonify(response), status_code

@routes.route('/getUsersCompanies', methods=['GET'])
def get_users_companies():
    request_data = json.loads(request.args.to_dict()['query'])
    response = handle_get_users_companies(request_data)
    return jsonify(response)
