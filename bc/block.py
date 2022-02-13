from hashlib import sha256
import json

class Block(object):
    def __init__(self, index, transactions, time, previous_hash, nonce=0):
        self.index=index
        self.transactions=transactions
        self.time=time
        self.previous_hash=previous_hash
        self.nonce=nonce

    def compute_hash(self):
        block_string=json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()