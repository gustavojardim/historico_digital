from flask import Blueprint, request, jsonify
from off_chain_api.app_setup import db
from off_chain_api.model.user import User, user_schema
from off_chain_api.model.car import car_schema

UNREGISTERED_USER_MESSAGE = 'User not registered'
LOGIN_ALREADY_EXISTS = 'E-mail already in use'

auth_routes = Blueprint('auth_routes', __name__, template_folder='routes')

@auth_routes.route('/login/<email>', methods=['GET'])
def login(email):
    user = fetch_user(email)
    user = user_schema.dump(user)
    if user is not None:
        user['cars'] = car_schema.dump(user['cars'])
        return jsonify(user), 200
    return UNREGISTERED_USER_MESSAGE, 400

@auth_routes.route('/register', methods=['POST'])
def register():
    parameters = request.json

    e_mail = parameters['e_mail']

    if fetch_user(e_mail):
        return LOGIN_ALREADY_EXISTS, 403

    name = parameters['name']
    salt = parameters['salt']
    password = parameters['password']
    registration = parameters['registration']

    if len(registration) == 11:
        user_type_id = 1
    else:
        user_type_id = 2

    new_user = User(registration, name, e_mail, password, salt, user_type_id)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 200

def fetch_user(email):
    return User.query.filter_by(email=email).first()
