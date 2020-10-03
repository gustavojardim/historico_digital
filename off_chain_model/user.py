from back_end.app_setup import db
from back_end.app_setup import marsh

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(60))
    name = db.Column(db.String(60))
    email = db.Column(db.String(18))
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