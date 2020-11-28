from off_chain_api.app_setup import db
from off_chain_api.app_setup import marsh

class Car(db.Model):
    __tablename__ = 'car'

    car_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    license_plate = db.Column(db.String(7), nullable=False, unique=True)
    mileage = db.Column(db.String(7), nullable=False)
    node_id = db.Column(db.Integer, db.ForeignKey('node.node_id'))

    node = db.relationship('Node', primaryjoin='Car.node_id == Node.node_id', backref='cars')
    user = db.relationship('User', primaryjoin='Car.user_id == User.user_id', backref='cars')

    def __init__(self, user_id, license_plate, mileage, node_id):
        self.user_id = user_id
        self.license_plate = license_plate
        self.mileage = mileage
        self.node_id = node_id

class CarSchema(marsh.Schema):
    class Meta:
        fields = ('car_id', 'user_id', 'license_plate', 'mileage', 'node_id')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)
