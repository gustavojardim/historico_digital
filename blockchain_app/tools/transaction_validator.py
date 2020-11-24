class TransactionValidator(object):
    def __init__(self):
        pass

    def validate(self, last_block, current_transaction):
        # validates current_mileage is equal or greater than the last
        # validates if the token is of permission is valid
        if current_transaction['token'] == 'invalid':
            return False

        if not last_block.transaction:
            return True

        if int(last_block.transaction['mileage']) < current_transaction['mileage']:
            return True

        return False
