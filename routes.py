import json

from flask import Blueprint, request
from app_setup import db, blockchain

from tools.transaction_validator import TransactionValidator

from off_chain_model.car import Car, car_schema, cars_schema
from off_chain_model.user import User, user_schema, users_schema
from off_chain_model.vendor import Vendor, vendor_schema, vendors_schema
from off_chain_model.service import Service, service_schema, services_schema

routes_bp = Blueprint('routes', __name__, template_folder='back_end')

@routes_bp.route('/new_service', methods=['POST'])
def new_service():
    tx_data = request.get_json()
    required_fields = ["current_owner_cpf", "vendor_cnpj", "license_plate",
                       "service_type", "service_description", "current_mileage_in_km", "token"]

    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid transaction data: missing required field", 404

    tx_validator = TransactionValidator()

    if tx_validator.validate(blockchain.last_block_by_license_plate(tx_data['license_plate']), tx_data):
        new_block = blockchain.add_new_block(tx_data)
        if new_block:
            b_hash = new_block.hash
            block_number = new_block.index

            car = Car.query.filter_by(license_plate=tx_data['license_plate']).all()
            vendor = Vendor.query.filter_by(cnpj=tx_data['vendor_cnpj']).all()

            car = car[0]
            vendor = vendor[0]

            car_id = car.car_id
            user_id = car.user_id
            vendor_id = vendor.vendor_id
            new_service = Service(b_hash, block_number, car_id, user_id, vendor_id)

            print(new_service)

            db.session.add(new_service)
            db.session.commit()
            return "Success", 201

    return "Invalid transaction data: invalid token or mileage", 404

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

# @routes_bp.route('/chain', methods=['GET'])
# def get_chain():
#     chain_data = []
#     for block in blockchain.chain:
#         chain_data.append(block.__dict__)
#     return json.dumps({"length": len(chain_data),
#                        "chain": chain_data})

@routes_bp.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    block_dict = {}

    for block in blockchain.chain:
        block_dict = block.__dict__
        if block_dict['transaction']:
            print(block_dict)
            vendor = Vendor.query.filter_by(cnpj=block_dict['transaction']['vendor_cnpj']).all()
            vendor = vendor[0]
            block_dict['transaction']['vendor_name'] = vendor.name
            chain_data.append(block_dict)
    return json.dumps(chain_data)

@routes_bp.route('/chain/<license_plate>', methods=['GET'])
def get_chain_by_license_plate(license_plate):
    chain_data = []
    block_dict = {}
    car = Car.query.filter_by(license_plate=license_plate).all()
    car_id = car[0].car_id
    services = Service.query.filter_by(car_id=car_id).all()

    for service in services:
        for block in blockchain.chain:
            if block.index == service.block_number:
                block_dict = block.__dict__
                print(block_dict)
                vendor = Vendor.query.filter_by(cnpj=block_dict['transaction']['vendor_cnpj']).all()
                vendor = vendor[0]
                block_dict['transaction']['vendor_name'] = vendor.name
                chain_data.append(block_dict)
    return json.dumps(chain_data)
