from flask import Blueprint, jsonify, request
from off_chain_api.app_setup import db
from off_chain_api.model.user_type import UserType, user_type_schema, user_types_schema

user_type_routes = Blueprint('user_type_routes', __name__, template_folder='routes')

@user_type_routes.route('/user_type', methods=['GET'])
def get_all():
    all_user_types = UserType.query.all()
    results = user_types_schema.dump(all_user_types)
    return jsonify(results)

@user_type_routes.route('/user_type/<user_type_id>', methods=['GET'])
def get(user_type_id):
    return user_type_schema.jsonify(UserType.query.get(user_type_id))

@user_type_routes.route('/user_type/type_code/<type_code>', methods=['GET'])
def get_by_type_code(type_code):
    user_type = UserType.query.filter_by(type_code=type_code).first()
    return user_type_schema.jsonify(user_type)

@user_type_routes.route('/user_type', methods=['POST'])
def add():
    parameters = request.json

    type_code = parameters['type_code']
    type_description = parameters['type_description']

    new_user_type = UserType(type_code, type_description)

    db.session.add(new_user_type)
    db.session.commit()
    return user_type_schema.jsonify(new_user_type)

@user_type_routes.route('/user_type/<user_type_id>', methods=['PUT'])
def update(user_type_id):
    parameters = request.json

    user_type = UserType.query.get(user_type_id)

    user_type.type_code = parameters['type_code']
    user_type.type_description = parameters['type_description']

    db.session.commit()
    return user_type_schema.jsonify(user_type)

