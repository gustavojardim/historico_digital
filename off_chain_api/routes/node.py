from flask import Blueprint, jsonify, request
from off_chain_api.app_setup import db
from off_chain_api.model.node import Node, node_schema, nodes_schema

node_routes = Blueprint('node_routes', __name__, template_folder='routes')

@node_routes.route('/node', methods=['GET'])
def get_all():
    all_nodes = Node.query.all()
    results = nodes_schema.dump(all_nodes)
    return jsonify(results)

@node_routes.route('/node/<node_id>', methods=['GET'])
def get(node_id):
    return node_schema.jsonify(Node.query.get(node_id))

@node_routes.route('/node/alias/<alias>', methods=['GET'])
def get_by_alias(alias):
    node = Node.query.filter_by(alias=alias).first()
    return node_schema.jsonify(node)

@node_routes.route('/node', methods=['POST'])
def add():
    parameters = request.json

    alias = parameters['alias']
    ip_address = parameters['ip_address']

    new_node = Node(ip_address, alias)

    db.session.add(new_node)
    db.session.commit()
    return node_schema.jsonify(new_node)

@node_routes.route('/node/<node_id>', methods=['PUT'])
def update(node_id):
    parameters = request.json

    node = Node.query.get(node_id)

    node.alias = parameters['alias']
    node.active = parameters['active']
    node.ip_address = parameters['ip_address']

    db.session.commit()
    return node_schema.jsonify(node)
