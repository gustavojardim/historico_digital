from off_chain_api.app_setup import db
from off_chain_api.app_setup import marsh


class UserType(db.Model):
    __tablename__ = 'user_type'

    user_type_id = db.Column(db.Integer, primary_key=True)
    type_code = db.Column(db.String(2), nullable=False, unique=True)
    type_description = db.Column(db.String(32), nullable=False)

    def __init__(self, type_code, type_description):
        self.type_code = type_code
        self.type_description = type_description

class UserTypeSchema(marsh.Schema):
    class Meta:
        fields = ('user_type_id', 'type_code', 'type_description')

user_type_schema = UserTypeSchema()
user_types_schema = UserTypeSchema(many=True)

