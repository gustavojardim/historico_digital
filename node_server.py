import json
import requests

from blockchain import Blockchain
from app_setup import app, blockchain
from block import Block

from routes import routes_bp

# the address to other participating members of the network
peers = set()

app = app

app.register_blueprint(routes_bp)

# Uncomment this line if you want to specify the port number in the code
app.run(debug=True, port=8000)
