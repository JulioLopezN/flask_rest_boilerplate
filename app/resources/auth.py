from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, render_template, g
from sqlalchemy.exc import IntegrityError
from app import jwt_manager, bcrypt, ma, db, email_sender
from app.models import User
from app.schemas import LoginSchema, RegisterSchema
from app.common.constants.roles import Roles
from app.common.security.password_helpers import password_generate
from app.common.decorators.authorized import authorized

auth_api = Blueprint('auth', __name__, url_prefix='/auth')


@auth_api.route('/login', methods=['POST'])
def login():
    model = LoginSchema().load(request.json)
    user = User.query.filter_by(email=model['email'], active=True).first()

    if not user or not bcrypt.check_password_hash(user.password_hash, model['password']):
        return {'message': 'Invalid username or password'}

    payload = {
        'id_user': user.id_user,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'roles': user.roles,
    }

    token = jwt_manager.encode(payload, model['remember_me'])

    return {'token': token.decode('utf-8'), 'expire': payload['exp']}


@auth_api.route('/register', methods=['POST'])
def register():
    try:
        model = RegisterSchema().load(request.json)

        user = User()

        user.email = model['email']
        user.first_name = model['first_name']
        user.last_name = model['last_name']
        user.password_hash = bcrypt.generate_password_hash(model['password'])
        user.active = True
        user.roles = ','.join([Roles.CUSTOMER.value])

        db.session.add(user)
        db.session.commit()

        payload = {
            'id_user': user.id_user,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'roles': user.roles,
        }

        token = jwt_manager.encode(payload)

        return {'token': token.decode('utf-8'), 'expire': payload['exp']}
    except IntegrityError as ex:
        return {'error': 'Data integrity error'}, 400


@auth_api.route('/change_password', methods=['PUT'])
@authorized()
def change_password():
    model = request.json
    user_session = g.user

    user = User.query.filter_by(id_user=user_session['id_user'], active=True).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, model['old_password']):
        return { 'error': 'invalid password' }, 400

    if model['new_password'] != model['confirm_password']:
        return { 'error': 'please confirm password correctly' }, 400
    
    user.password_hash = bcrypt.generate_password_hash(model['new_password'])
    
    db.session.commit()

    return '', 204


@auth_api.route('/reset_password', methods=['POST'])
def reset_password():
    model = request.json

    user = User.query \
        .filter_by(email=model['email'], active=True) \
        .first()

    if not user:
        return '', 204

    user.reset_password_expire = datetime.utcnow() + timedelta(days=1)
    user.reset_password_token = password_generate(32)

    db.session.commit()

    template = render_template('emails/reset_password.html', user=user)
    
    try:
        email_sender.send(template, user.email)
        return '', 204
    except:
        return '', 503

@auth_api.route('/confirm_reset_password', methods=['PUT'])
def confirm_reset_password():
    model = request.json

    user = User.query \
        .filter_by(
            id_user=model['id_user'], 
            reset_password_token=model['reset_password_token'], 
            active=True
        ) \
        .first()

    if not user:
        return '', 400

    if user.reset_password_expire < datetime.utcnow():
        return { 'error': 'Token expired' }, 400

    user.password_hash = bcrypt.generate_password_hash(model['password'])
    user.reset_password_token = None
    user.reset_password_expire = None
    
    db.session.commit()

    payload = {
        'id_user': user.id_user,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'roles': user.roles,
    }

    token = jwt_manager.encode(payload)

    return {'token': token.decode('utf-8'), 'expire': payload['exp']}
