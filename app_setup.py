from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from back_end.blockchain import Blockchain

HOST = '127.0.0.1'
SERVER = 'postgres'
PORT = '5432'
DATABASE = 'postgres'
DRIVER = 'Devart ODBC Driver for PostgreSQL'
USERNAME = 'postgres'
PASSWORD = ''

print(HOST)
print(SERVER)
print(USERNAME)
print(PASSWORD)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
marsh = Marshmallow(app)
