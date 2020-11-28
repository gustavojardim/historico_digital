from flask import Blueprint, jsonify, request
from off_chain_api.app_setup import db
from off_chain_api.model.user import User, user_schema, users_schema

user_routes = Blueprint('user_routes', __name__, template_folder='routes')

@user_routes.route('/user', methods=['GET'])
def get_all():
    all_users = User.query.all()
    results = users_schema.dump(all_users)
    return jsonify(results)

@user_routes.route('/user/<user_id>', methods=['GET'])
def get(user_id):
    return user_schema.jsonify(User.query.get(user_id))

@user_routes.route('/user/email/<email>', methods=['GET'])
def get_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user_schema.jsonify(user)

@user_routes.route('/user/registration/<registration>', methods=['GET'])
def get_by_registration(registration):
    user = User.query.filter_by(registration=registration).first()
    return user_schema.jsonify(user)

@user_routes.route('/user', methods=['POST'])
def add():
    parameters = request.json

    name = parameters['name']
    salt = parameters['salt']
    email = parameters['email']
    password = parameters['password']
    registration = parameters['registration']
    user_type_id = parameters['user_type_id']

    new_user = User(registration, name, email, password, salt, user_type_id)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


@user_routes.route('/user/<user_id>', methods=['PUT'])
def update(user_id):
    parameters = request.json

    user = User.query.get(user_id)

    user.name = parameters['name']
    user.salt = parameters['salt']
    user.email = parameters['email']
    user.password = parameters['password']
    user.registration = parameters['registration']
    user.user_type_id = parameters['user_type_id']

    db.session.commit()
    return user_schema.jsonify(user)
