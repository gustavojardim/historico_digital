from off_chain_api.app_setup import db
from off_chain_api.app_setup import marsh

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    registration = db.Column(db.String(14), nullable=False, unique=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    salt = db.Column(db.Text)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.user_type_id'))
    cars = db.relationship('Car', backref='Owner', primaryjoin='Car.user_id==User.user_id')

    user_type = db.relationship('UserType', primaryjoin='User.user_type_id == UserType.user_type_id', backref='users')

    def __init__(self, registration, name, email, password, salt, user_type_id):
        self.name = name
        self.salt = salt
        self.email = email
        self.password = password
        self.registration = registration
        self.user_type_id = user_type_id

class UserSchema(marsh.Schema):
    class Meta:
        fields = ('user_id', 'registration', 'name', 'email', 'password', 'salt', 'cars', 'user_type_id')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
