from flask import Blueprint, jsonify, request
from off_chain_api.app_setup import db
from off_chain_api.model.car import Car, car_schema, cars_schema

car_routes = Blueprint('car_routes', __name__, template_folder='routes')

@car_routes.route('/car', methods=['GET'])
def get_all():
    all_cars = Car.query.all()
    results = cars_schema.dump(all_cars)
    return jsonify(results)

@car_routes.route('/car/<car_id>', methods=['GET'])
def get(car_id):
    return car_schema.jsonify(Car.query.get(car_id))

@car_routes.route('/car/license_plate/<license_plate>', methods=['GET'])
def get_by_license_plate(license_plate):
    car = Car.query.filter_by(license_plate=license_plate).first()
    return car_schema.jsonify(car)

@car_routes.route('/car/owner/<user_id>', methods=['GET'])
def get_by_owners(user_id):
    cars = Car.query.filter_by(user_id=user_id).all()
    results = cars_schema.dump(cars)
    return jsonify(results)

@car_routes.route('/car', methods=['POST'])
def add():
    parameters = request.json

    user_id = parameters['user_id']
    node_id = parameters['node_id']
    mileage = parameters['mileage']
    license_plate = parameters['license_plate']

    new_car = Car(user_id, license_plate, mileage, node_id)

    db.session.add(new_car)
    db.session.commit()
    return car_schema.jsonify(new_car)

@car_routes.route('/car/<car_id>', methods=['PUT'])
def update(car_id):
    parameters = request.json

    car = Car.query.get(car_id)

    car.user_id = parameters['user_id']
    car.node_id = parameters['node_id']
    car.mileage = parameters['mileage']
    car.license_plate = parameters['license_plate']

    db.session.commit()
    return car_schema.jsonify(car)
