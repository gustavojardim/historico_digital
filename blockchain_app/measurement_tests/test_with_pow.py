from blockchain_app.measurement_tests.blockchain_with_pow import BlockchainPow

import time
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)


if __name__ == "__main__":
    blockchain = BlockchainPow()
    blockchain.create_genesis_block()

    total_time = 0
    total_tries = 0

    for i in range(100):
        transaction = {"test1" : "test"+str(i),
                       "test2" : "test"+str(i),
                       "test3" : "test"+str(i),
                       "test4" : "test"+str(i),
                       "test5" : "test"+str(i)}
        blockchain.add_new_transaction(transaction)

        start_time = time.time()
        total_tries += blockchain.mine()
        total_time = total_time + (time.time() - start_time)

    avg_time = total_time/100
    avg_tries = total_tries/100

    print(avg_time)
    print(avg_tries)
