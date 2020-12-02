import json
from datetime import datetime

from hashlib import sha256

class Block:
    def __init__(self, index, transaction, timestamp, previous_hash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.date = datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y')
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
