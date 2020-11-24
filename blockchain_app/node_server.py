import json
import requests

from blockchain_app.application_setup import app, blockchain
from blockchain_app.blockchain import Blockchain
from blockchain_app.block import Block

from blockchain_app.routes import routes_bp

# the address to other participating members of the network
peers = set()

app = app

app.register_blueprint(routes_bp)

# Uncomment this line if you want to specify the port number in the code
app.run(debug=True, port=8000)
