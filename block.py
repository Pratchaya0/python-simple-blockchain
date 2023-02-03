import hashlib
import transection as tx

class Block:
    def __init__(self, data, previous_hash, index):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8') + self.previous_hash.encode('utf-8') + str(self.index).encode('utf-8'))
        return sha.hexdigest()
    
    def txs_count(self):
        if isinstance(self.data, list):
            return len(self.data)
        elif isinstance(self.data, tx.Customer):
            return 1
        else:
            return 0