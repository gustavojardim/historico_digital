from off_chain_api.app_setup import db
from off_chain_api.app_setup import marsh

class Node(db.Model):
    __tablename__ = 'node'

    node_id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(32), nullable=False, unique=True)
    alias = db.Column(db.String(16), nullable=False, unique=True)
    active = db.Column(db.BIT(1), nullable=False)

    def __init__(self, ip_address, alias):
        self.ip_address = ip_address
        self.alias = alias
        self.active = True

class NodeSchema(marsh.Schema):
    class Meta():
        fields = ('node_id', 'ip_adress', 'alias', 'active')

node_schema = NodeSchema()
nodes_schema = NodeSchema(many=True)
