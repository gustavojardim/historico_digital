from app_setup import db
from app_setup import marsh

class Service(db.Model):
    __tablename__ = 'SERVICE'
    service_id = db.Column(db.Integer, primary_key=True)
    block_hash = db.Column(db.String(60))
    car_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer)

    def __init__(self, block_hash, car_id, user_id, vendor_id):
        self.block_hash = block_hash
        self.car_id = car_id
        self.user_id = user_id
        self.vendor_id = vendor_id

class ServiceSchema(marsh.Schema):
    class Meta:
        fields = ('service_id', 'block_hash', 'car_id', 'user_id', 'vendor_id')

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
