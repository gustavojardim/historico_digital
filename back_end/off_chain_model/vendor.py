from app_setup import db
from app_setup import marsh

class Vendor(db.Model):
    __tablename__ = 'VENDOR'
    vendor_id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(60))
    email = db.Column(db.String(18))
    password = db.Column(db.String(12))

    def __init__(self, cnpj, email, password):
        self.cnpj = cnpj
        self.email = email
        self.password = password

class VendorSchema(marsh.Schema):
    class Meta:
        fields = ('vendor_id', 'cnpj', 'email', 'password')

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)
