from blockchain_app.blockchain import Blockchain

import time
import json

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.create_genesis_block()

    total_time = 0


    for i in range(100):
        start_time = time.time()
        blockchain.add_new_block({"test1" : "test"+str(i),
                                  "test2" : "test"+str(i),
                                  "test3" : "test"+str(i),
                                  "test4" : "test"+str(i),
                                  "test5" : "test"+str(i)})
        total_time = total_time + (time.time() - start_time)

    # blocks = []

    # for block in reversed(blockchain.chain):

    #     blocks.append(block.__dict__)

    # with open('data.json', 'w') as fp:
    #     json.dump(blocks, fp)

    avg_time = total_time / 100

    print("Total time", total_time)
    print("Average time", avg_time)
