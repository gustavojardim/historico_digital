import time

from blockchain_app.block import Block

class Blockchain:

    def __init__(self):
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

    def last_block_by_license_plate(self, license_plate):
        print(license_plate, 'given_lp')
        if len(self.chain) > 1:
            for block in reversed(self.chain):
                try:
                    last_block_license_plate = block.transaction['license_plate']
                except TypeError:
                    print('except')
                    print(self.chain[0])
                    return self.chain[0]
                print(block, 'block')
                print(last_block_license_plate)
                if last_block_license_plate == license_plate:
                    return block
            #return self.chain[0]
        return self.last_block

    def add_new_block(self, transaction):
        new_block = Block(index=self.last_block.index + 1,
                          transaction=transaction,
                          timestamp=time.time(),
                          previous_hash=self.last_block.hash)

        previous_hash = self.last_block.hash

        if previous_hash != new_block.previous_hash:
            return None

        self.chain.append(new_block)

        return new_block

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
