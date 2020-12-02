import json
import requests

from flask import Blueprint, request

from blockchain_app.blockchain_setup import blockchain
from blockchain_app.tools.transaction_validator import TransactionValidator

routes = Blueprint('routes', __name__, template_folder='blockchain_app')

OFF_CHAIN_API_URL = 'http://127.0.0.1:5000'

@routes.route('/new_service', methods=['POST'])
def new_service():
    tx_data = request.get_json()
    required_fields = ["owner_cpf", "vendor_cnpj", "vendor_name", "license_plate",
                       "service_type", "service_description", "mileage", "token"]

    for field in required_fields:
        if not tx_data.get(field):
            print(field)
            return "Invalid transaction data: missing required field", 404

    tx_validator = TransactionValidator()

    if tx_validator.validate(blockchain.last_block_by_license_plate(tx_data['license_plate']), tx_data):
        new_block = blockchain.add_new_block(tx_data)
        if new_block is not None:
            print('oloco')
            param = {
                'license_plate' : tx_data['license_plate'],
                'vendor_id' : tx_data['vendor_id'],
                'mileage' : tx_data['mileage']
            }
            requests.post(OFF_CHAIN_API_URL + '/service', json=json.loads(json.dumps(param)))
            return 201

    return "Invalid transaction data: invalid token or mileage", 404

@routes.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    block_dict = {}

    for block in blockchain.chain:
        block_dict = block.__dict__
        if block_dict['transaction']:
            print(block_dict)
            chain_data.append(block_dict)
    return json.dumps(chain_data)

@routes.route('/chain/<registration>', methods=['GET'])
def get_chain_by_registration(registration):
    chain_data = []
    block_dict = {}

    if len(registration) > 11:
        registration_type = 'vendor_cnpj'
    else:
        registration_type = 'owner_cpf'

    for block in blockchain.chain:
        block_dict = block.__dict__
        if block_dict['transaction']:
            if block_dict['transaction'][registration_type] == registration:
                chain_data.append(block_dict)
    return json.dumps(chain_data)
