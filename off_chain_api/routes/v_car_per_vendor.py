from flask import Blueprint, jsonify, request
from off_chain_api.app_setup import db
from off_chain_api.model.v_car_per_vendor import VCarPerVendor, v_cars_per_vendor_schema

v_car_per_vendor_routes = Blueprint('v_car_per_vendor_routes', __name__, template_folder='routes')

@v_car_per_vendor_routes.route('/v_car_per_vendor/<registration>', methods=['GET'])
def get(registration):
    return v_cars_per_vendor_schema.jsonify(VCarPerVendor.query.filter_by(registration=registration).all())
