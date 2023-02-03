import hashlib

class Block:
    def __init__(self, transaction, previous_hash, index):
        self.index = index
        self.data = transaction
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        for tx in self.data:
            sha.update(tx.hash.encode('utf-8'))
        sha.update(self.previous_hash.encode('utf-8') + str(self.index).encode('utf-8'))
        return sha.hexdigest()

    def txs_count(self):
        return len(self.data)