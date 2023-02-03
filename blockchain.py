import block as b

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return b.Block([], "0", 0)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        block = b.Block(data, previous_block.hash, previous_block.index + 1)
        self.chain.append(block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if previous_block.hash != current_block.previous_hash:
                return False
        return True

    def update_block_data(self, index, new_data):
        if index >= len(self.chain):
            print("Block index out of range.")
            return

        block_to_update = self.chain[index]
        block_to_update.data = new_data
        block_to_update.hash = block_to_update.calculate_hash()

    def get_transactions_by_owner_name(self, owner_name):
        result = []
        for block in self.chain:
            for tx in block.data:
                if tx.title_deed.owner == owner_name:
                    result.append(tx)
        return result
    
    def get_block_by_tx_hash(self, tx_hash):
        for block in self.chain:
            for tx in block.data:
                if tx.hash == tx_hash:
                    return block.index
        return None
    
    def block_count(self):
        return len(self.chain)
    
    def selectBlock(self, index):
        for block in self.chain:
            if block.index == index:
                return block
        return None
