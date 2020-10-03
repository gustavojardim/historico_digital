from back_end.app_setup import db
from back_end.app_setup import marsh

class Vendor(db.Model):
    __tablename__ = 'vendor'
    vendor_id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(60))
    name = db.Column(db.String(60))
    email = db.Column(db.String(18))
    password = db.Column(db.String(12))

    def __init__(self, cnpj, name, email, password):
        self.cnpj = cnpj
        self.name = name
        self.email = email
        self.password = password

class VendorSchema(marsh.Schema):
    class Meta:
        fields = ('vendor_id', 'cnpj', 'name', 'email', 'password')

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)
