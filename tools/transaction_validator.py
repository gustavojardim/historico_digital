class TransactionValidator(object):
    def __init__(self):
        pass

    def validate(self, last_transaction, current_transaction):
        # validates current_mileage is equal or greater than the last
        # validates if the token is of permission is valid
        if last_transaction['current_mileage_in_km'] < current_transaction['current_mileage_in_km']:
            return False
        return True
