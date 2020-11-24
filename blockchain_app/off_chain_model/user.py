from application_setup import db
from application_setup import marsh

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11))
    name = db.Column(db.String(128))
    email = db.Column(db.String(64))
    password = db.Column(db.String(12))
    cars = db.relationship('off_chain_model.car.Car', backref='User', primaryjoin='off_chain_model.car.Car.user_id==User.user_id')

    def __init__(self, cpf, name, email, password):
        self.cpf = cpf
        self.name = name
        self.email = email
        self.password = password

class UserSchema(marsh.Schema):
    class Meta:
        fields = ('user_id', 'cpf', 'name', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
