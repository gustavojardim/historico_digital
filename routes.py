import json

from flask import Blueprint, request
from back_end.app_setup import db, blockchain

from back_end.tools.transaction_validator import TransactionValidator

from back_end.off_chain_model.car import Car, car_schema, cars_schema
from back_end.off_chain_model.user import User, user_schema, users_schema
from back_end.off_chain_model.vendor import Vendor, vendor_schema, vendors_schema

routes_bp = Blueprint('routes', __name__, template_folder='back_end')

@routes_bp.route('/new_service', methods=['POST'])
def new_service():
    tx_data = request.get_json()
    required_fields = ["current_owner_cpf", "vendor_cnpj", "license_plate",
                       "service_type", "service_description", "current_mileage_in_km", "token"]

    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid transaction data", 404

    blockchain = Blockchain()
    blockchain.create_genesis_block()

    tx_validator = TransactionValidator()

    if tx_validator.validate(blockchain.last_block.transaction, tx_data):
        blockchain.add_new_block(tx_data)
        return "Success", 201
    else:
        return "Invalid transaction data", 404

@routes_bp.route('/new_vendor', methods=['POST'])
def new_vendor():
    name = request.json['name']
    cnpj = request.json['cnpj']
    email = request.json['email']
    password = request.json['password']

    new_vendor = Vendor(cnpj, name, email, password)

    db.session.add(new_vendor)
    db.session.commit()

    return vendor_schema.jsonify(new_vendor)

@routes_bp.route('/new_user', methods=['POST'])
def new_user():
    name = request.json['name']
    cpf = request.json['cpf']
    email = request.json['email']
    password = request.json['password']

    new_user = User(cpf, name, email, password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@routes_bp.route('/new_car', methods=['POST'])
def new_car():
    user_id = request.json['user_id']
    license_plate = request.json['license_plate']
    current_mileage_in_km = request.json['current_mileage_in_km']

    new_car = Car(user_id, license_plate, current_mileage_in_km)

    db.session.add(new_car)
    db.session.commit()

    return car_schema.jsonify(new_car)

@routes_bp.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
