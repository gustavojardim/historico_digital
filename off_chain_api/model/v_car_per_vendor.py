from off_chain_api.app_setup import db
from off_chain_api.app_setup import marsh

class VCarPerVendor(db.Model):
    __tablename__ = 'v_car_per_vendor'

    vendor_id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(7))
    registration = db.Column(db.String(14))

class VCarPerVendor(marsh.Schema):
    class Meta:
        fields = ('vendor_id', 'license_plate', 'registration')

v_car_per_vendor_schema = VCarPerVendor()
v_cars_per_vendor_schema = VCarPerVendor(many=True)

