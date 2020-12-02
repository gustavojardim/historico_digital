from off_chain_api.app_setup import app

from off_chain_api.routes.car import car_routes
from off_chain_api.routes.auth import auth_routes
from off_chain_api.routes.node import node_routes
from off_chain_api.routes.user import user_routes
from off_chain_api.routes.service import service_routes
from off_chain_api.routes.user_type import user_type_routes
from off_chain_api.routes.v_car_per_vendor import v_car_per_vendor_routes

app = app

app.register_blueprint(car_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(node_routes)
app.register_blueprint(user_routes)
app.register_blueprint(service_routes)
app.register_blueprint(user_type_routes)
app.register_blueprint(v_car_per_vendor_routes)

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='127.0.0.1', port=5000, debug=True)
