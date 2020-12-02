import json
import requests

from flask import Flask
from blockchain_app.routes import routes

app = Flask(__name__)

app.register_blueprint(routes)

# Uncomment this line if you want to specify the port number in the code
app.run(debug=True, port=8080)
