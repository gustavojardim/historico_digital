from app_setup import db
from app_setup import marsh

class Car(db.Model):
    __tablename__ = 'car'
    car_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    license_plate = db.Column(db.String(7))
    current_mileage_in_km = db.Column(db.String(7))

    def __init__(self, user_id, license_plate, current_mileage_in_km):
        self.user_id = user_id
        self.license_plate = license_plate
        self.current_mileage_in_km = current_mileage_in_km

class CarSchema(marsh.Schema):
    class Meta:
        fields = ('car_id', 'user_id', 'license_plate', 'current_mileage_in_km')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)
