from app_setup import db
from app_setup import marsh

class Car(db.Model):
    __tablename__ = 'CAR'
    car_id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(60))
    current_mileage_in_km = db.GIColumn(db.String(18))

    def __init__(self, cpf, email, password):
        self.cpf = cpf
        self.email = email
        self.password = password

class CarSchema(marsh.Schema):
    class Meta:
        fields = ('user_id', 'cpf', 'email', 'password')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)
