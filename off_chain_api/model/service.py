from off_chain_api.app_setup import db
from off_chain_api.app_setup import marsh

class Service(db.Model):
    __tablename__ = 'service'

    service_id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.car_id', ondelete='SET NULL'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)

    car = db.relationship('Car', primaryjoin='Service.car_id == Car.car_id', backref='services')
    vendor = db.relationship('User', primaryjoin='Service.vendor_id == User.user_id', backref='services')

    def __init__(self, car_id, vendor_id):
        self.car_id = car_id
        self.vendor_id = vendor_id

class ServiceSchema(marsh.Schema):
    class Meta:
        fields = ('service_id', 'car_id', 'vendor_id')

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
