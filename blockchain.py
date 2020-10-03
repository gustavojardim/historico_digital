import time

from back_end.block import Block

class Blockchain:

    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.chain = []

    def create_genesis_block(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        genesis_block = Block(0, [], 0, "0")
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_new_block(self, transaction):
        new_block = Block(index=self.last_block.index + 1,
                          transaction=transaction,
                          timestamp=time.time(),
                          previous_hash=self.last_block.hash)

        previous_hash = self.last_block.hash

        if previous_hash != new_block.previous_hash:
            return False

        self.chain.append(new_block)

        return True

    def persist_blockchain(self):
        pass

    @classmethod
    def check_chain_validity(cls, chain):
        result = True
        previous_hash = "0"

        for block in chain:
            block_hash = block.hash
            # remove the hash field to recompute the hash again
            # using `compute_hash` method.
            delattr(block, "hash")

            if previous_hash != block.previous_hash:
                result = False
                break

            block.hash, previous_hash = block_hash, block_hash

        return result
