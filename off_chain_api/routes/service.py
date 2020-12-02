from flask import Blueprint, jsonify, request
from off_chain_api.app_setup import db
from off_chain_api.model.service import Service, service_schema, services_schema
from off_chain_api.model.car import Car

service_routes = Blueprint('service_routes', __name__, template_folder='routes')

@service_routes.route('/service', methods=['GET'])
def get_all():
    all_services = Service.query.all()
    return jsonify(services_schema.dump(all_services))


@service_routes.route('/service/<service_id>', methods=['GET'])
def get(service_id):
    return service_schema.jsonify(Service.query.get(service_id))

@service_routes.route('/service', methods=['POST'])
def add():
    parameters = request.json

    car = Car.query.filter_by(license_plate=parameters['license_plate']).first()

    car_id = car.car_id
    vendor_id = parameters['vendor_id']

    service = Service(car_id, vendor_id)

    db.session.add(service)
    db.session.commit()
    return service_schema.jsonify(service)
