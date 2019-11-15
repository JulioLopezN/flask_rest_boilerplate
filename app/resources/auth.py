from datetime import datetime
from flask import Blueprint, request, jsonify
from app import jwt_manager, bcrypt, ma
from app.models import User
from app.schemas import LoginSchema

auth_api = Blueprint('auth', __name__, url_prefix='/auth')

login_schema = LoginSchema()


@auth_api.route('/login', methods=['POST'])
def login():
    model = login_schema.load(request.json)
    user = User.query.filter_by(email=model['username'], active=True).first()

    if not user or not bcrypt.check_password_hash(user.password_hash, model['password']):
        return {'message': 'Invalid username or password'}

    payload = {
        **model,
        'id_user': user.id_user,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'roles': user.roles,
    }

    token = jwt_manager.encode(payload, model['remember_me'])

    return {'token': token.decode('utf-8')}


@auth_api.route('/register', methods=['POST'])
def register():
    return {'message': datetime.utcnow().isoformat()}


@auth_api.route('/change_password', methods=['PUT'])
def change_password():
    return {'message': datetime.utcnow().isoformat()}


@auth_api.route('/reset_password', methods=['POST'])
def reset_password():
    return {'message': datetime.utcnow().isoformat()}


@auth_api.route('/confirm_reset_password', methods=['PUT'])
def confirm_reset_password():
    return {'message': datetime.utcnow().isoformat()}
