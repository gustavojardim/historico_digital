from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

HOST = os.getenv('DB_HOSTNAME')
SERVER = os.getenv('DB_SERVER_ADDRESS')
PORT = '1434'
DATABASE = 'PROD'
DRIVER = 'ODBC Driver 17 for SQL Server'
USERNAME = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASS')

print(HOST)
print(SERVER)
print(USERNAME)
print(PASSWORD)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://{USERNAME}:{PASSWORD}@{HOST}\{SERVER}:{PORT}/{DATABASE}?driver={DRIVER}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
marsh = Marshmallow(app)
