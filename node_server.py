import json
import requests

from back_end.blockchain import Blockchain
from back_end.app_setup import app, blockchain
from back_end.block import Block

from back_end.routes import routes_bp

# the address to other participating members of the network
peers = set()

app = app

app.register_blueprint(routes_bp)

# Uncomment this line if you want to specify the port number in the code
app.run(debug=True, port=8000)
