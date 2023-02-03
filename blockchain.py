import transection as tx
import block as b

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.index = 1

    def create_genesis_block(self):
        return b.Block("Genesis Block", "0", 0)

    def add_block(self, customers):
        previous_block = self.chain[-1]
        new_block = b.Block(customers, previous_block.hash, self.index)
        self.chain.append(new_block)
        self.index += 1
        
    def update_block_data(self, index, new_data):
        if index >= len(self.chain):
            print("Block index out of range.")
            return

        block_to_update = self.chain[index]
        block_to_update.data = new_data
        block_to_update.hash = block_to_update.calculate_hash()

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
    
    def selectBlock(self, index):
        for block in self.chain:
            if block.index == index:
                return block
        return None

    def selectDataByOwnerName(self, name_to_find):
        found_blocks = []
        for block in self.chain:
            if isinstance(block.data, tx.Customer) and block.data.name == name_to_find:
                found_blocks.append(block)
        return found_blocks if found_blocks else None
    
    def block_count(self):
        return len(self.chain)