import hashlib

class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Transaction:
    def __init__(self, customer):
        self.index = Transaction.get_index()
        self.customer = customer
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + self.customer.name.encode('utf-8') + self.customer.phone.encode('utf-8') + self.customer.email.encode('utf-8'))
        return sha.hexdigest()

    @staticmethod
    def get_index():
        if not hasattr(Transaction, "index"):
            Transaction.index = 0
        Transaction.index += 1
        return Transaction.index

class Block:
    def __init__(self, data, previous_hash, index):
        self.index = index
        self.data = data
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

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block([], "0", 0)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        block = Block(data, previous_block.hash, previous_block.index + 1)
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
    
    def update_transaction(self, customer_name, phone, email):
        for block in self.chain:
            for tx in block.data:
                if tx.customer.name == customer_name:
                    tx.customer.phone = phone
                    tx.customer.email = email
                    tx.hash = tx.calculate_hash()

    def get_transactions_by_customer_name(self, customer_name):
        result = []
        for block in self.chain:
            for tx in block.data:
                if tx.customer.name == customer_name:
                    result.append(tx)
        return result


# Select transactions by customer name
def select_txs_by_customer_name(blockchain, name):
    selected_txs = []
    for block in blockchain.chain:
        for tx in block.data:
            if tx.customer.name == name:
                selected_txs.append(tx)
    return selected_txs
# Test code for the Blockchain implementation

# Create customers
customer1 = Customer("John Doe", "+1234567890", "john.doe@example.com")
customer2 = Customer("Jane Doe", "+0987654321", "jane.doe@example.com")
customer3 = Customer("Jim Brown", "+1029384756", "jim.brown@example.com")

# Initialize a blockchain
blockchain = Blockchain()

# # Add transaction1
# transaction1 = Transaction(customer1)
# blockchain.add_block([transaction1])

# Add transactions to the blockchain
blockchain.add_block([Transaction(customer1), Transaction(customer2)])
blockchain.add_block([Transaction(customer3)])

# Check the integrity of the blockchain
if blockchain.is_valid():
    print("The blockchain is valid")
else:
    print("The blockchain is not valid")


selected_txs = select_txs_by_customer_name(blockchain, "John Doe")
print("Transactions for John Doe:")
for tx in selected_txs:
    print("Index: ", tx.index)
    print("Name: ", tx.customer.name)
    print("Phone: ", tx.customer.phone)
    print("Email: ", tx.customer.email)
    print("Hash: ", tx.hash)

# Update a customer
def update_customer(blockchain, name, new_phone, new_email):
    for block in blockchain.chain:
        for tx in block.data:
            if tx.customer.name == name:
                tx.customer.phone = new_phone
                tx.customer.email = new_email
                tx.hash = tx.calculate_hash()
                print("The customer has been updated")
                return
    print("The customer was not found")

update_customer(blockchain, "John Doe", "+6666666666", "john.doe@newemail.com")

selected_txs = select_txs_by_customer_name(blockchain, "John Doe")
print("Transactions for John Doe after update:")
for tx in selected_txs:
    print("Index: ", tx.index)
    print("Name: ", tx.customer.name)
    print("Phone: ", tx.customer.phone)
    print("Email: ", tx.customer.email)
    print("Hash: ", tx.hash)

# Check the integrity of the blockchain after update
if blockchain.is_valid():
    print("The blockchain is valid")
else:
    print("The blockchain is not valid")

