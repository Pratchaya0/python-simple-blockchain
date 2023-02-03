import transection as tx
import blockchain as bc

def show_block_data(block, num_of_tx):
    if block:
        print(f"Block index: {block.index}")
        print(f"Previous block hash: {block.previous_hash}")
        print("Block data:")
        print("Total customers:", block.txs_count())
        if block.txs_count() == 0:
            print(f"\t{block.data}")
        elif block.txs_count() == 1:
            print(f"\tCustomer name: {block.data.name}")
            print(f"\tCustomer phone number: {block.data.phone_number}")
            print(f"\tCustomer email: {block.data.email}")
        else:
            for customer in block.data:
                print(f"\tCustomer name: {customer.name}")
                print(f"\tCustomer phone number: {customer.phone_number}")
                print(f"\tCustomer email: {customer.email}")
        print(f"Block hash: {block.hash}")
    else:
        print(f"No block found with index: {block.index}")

def write_a_block():
    temp = 0
    tx_number = 1
    customer = []
    customers = []
    option_type = ["C", "W", "c", "w"]
    while True:
        if temp == 0:
            print(f"Input your {tx_number} Transection: ")
            tx_name = str(input("Name: "))
            tx_phone_number = str(input("Tel: "))
            tx_email = str(input("email: "))
            customer = tx.Customer(tx_name, tx_phone_number, tx_email)
            customers.append(customer)
            print(customers)
            tx_number += 1
            temp = 1
        elif temp == 11:
            break
        else:
            while True:
                print("----------------------------------------------------------------")
                option = str(input("Type (C) create next tx. or (W) exit [write a block] (C/W)?: "))
                if option in option_type:
                    if option == "C" or option == "c":
                        temp = 0
                    else:
                        if len(customers) == 1:
                            blockchain.add_block(customer)
                        else:
                            blockchain.add_block(customers)
                        temp = 11
                    break
                else:
                    print("Invalid Input! Please Input again")
                    
def update_block_data(block_index):
    temp = 0
    tx_number = 1
    customer = []
    customers = []
    option_type = ["C", "W", "c", "w"]
    while True:
        if temp == 0:
            print(f"Input your {tx_number} Transection: ")
            tx_name = str(input("Name: "))
            tx_phone_number = str(input("Tel: "))
            tx_email = str(input("email: "))
            customer = tx.Customer(tx_name, tx_phone_number, tx_email)
            customers.append(customer)
            print(customers)
            tx_number += 1
            temp = 1
        elif temp == 11:
            break
        else:
            while True:
                print("----------------------------------------------------------------")
                option = str(input("Type (C) create next tx. or (W) exit [write a block] (C/W)?: "))
                if option in option_type:
                    if option == "C" or option == "c":
                        temp = 0
                    else:
                        if len(customers) == 1:
                            blockchain.update_block_data(block_index, customer)
                        else:
                            blockchain.update_block_data(block_index, customers)
                        temp = 11
                    break
                else:
                    print("Invalid Input! Please Input again")

def check_blockchain_integrity():
    for i in range(1, blockchain.block_count()):
        current_block = blockchain.selectBlock(i)
        previous_block = blockchain.selectBlock(i-1)
        if current_block.previous_hash != previous_block.hash:
            print("\033[91m")
            print(f"Blockchain integrity compromised at block {i}")
            print("\033[0m")
            return 12
    print("\033[94m"+"Blockchain integrity intact."+"\033[0m")


# create a new blockchain
blockchain = bc.Blockchain()

# create some customer objects
customer1 = tx.Customer("John Smith", "+1 555 123 4567", "john.smith@example.com")
customer2 = tx.Customer("Jane Doe", "+1 555 789 1234", "jane.doe@example.com")
customer3 = tx.Customer("Bob Johnson", "+1 555 567 8901", "bob.johnson@example.com")
customer4 = tx.Customer("Jane Doe", "+1 555 789 8834", "jane.doe@example.com")

# add the customer objects to the blockchain
blockchain.add_block(customer1)
blockchain.add_block(customer2)
blockchain.add_block(customer3)
blockchain.add_block(customer4)

customers = [customer1, customer2, customer3, customer4]
blockchain.add_block(customers)

# check if the blockchain is valid
if blockchain.is_valid():
    print("The blockchain is valid.")
else:
    print("The blockchain is not valid.")   

while True:
    print("\033[92m")
    print("------------------------------- ASIGNMENT #1 ---------------------------------")
    print("======================== Welcome to Simply Blockchain ========================")
    print("Please select option")
    print("1. write a block")
    print("2. read a block")
    print("3. find your transection")
    print("4. Update date in block")
    print("5. Check block integrity")
    print("\033[0m")
    print("\033[91m"+"11. to exit"+"\033[0m")
    print("\n")
    option = int(input("=> "))
    if option:
        if option == 1:
            print("Hello world")
            write_a_block()
            # input def
        elif option == 2:
            print("Select read option")
            print("1. list all block and data")
            print("2. select block to list data")
            s_option = int(input("=> "))
            if s_option == 1:
                for i in range(0, blockchain.block_count()):
                    block = blockchain.selectBlock(i)
                    num_of_tx = block.txs_count()
                    print("\n============================================================== BLOCK #" + str(i))
                    show_block_data(block, num_of_tx)
                    print("============================================================== BLOCK #" + str(i) + "\n")
            elif s_option == 2:
                block_num = int(input("Input Block number=> "))
                block = blockchain.selectBlock(block_num)
                num_of_tx = block.txs_count()
                print("\n============================================================== BLOCK #" + str(block_num))
                show_block_data(block, num_of_tx)
                print("============================================================== BLOCK #" + str(block_num) + "\n")
        elif option == 3:
            name_to_find = str(input("Input you name=> "))
            found_blocks = blockchain.selectDataByOwnerName(name_to_find)
            if found_blocks:
                for block in found_blocks:
                    print("\n============================================================== BLOCK #" + str(block.index))
                    print(f"Found block with customer name: {block.data.name}")
                    print(f"Customer phone number: {block.data.phone_number}")
                    print(f"Customer email: {block.data.email}\n")
                    print("============================================================== BLOCK #" + str(block.index) + "\n")
            else:
                print(f"No block found with customer name: {name_to_find}")
        elif option == 4:
            block_index = int(input(f"You want to Edit data in Block #(0 -> {blockchain.block_count()-1})?: "))
            if block_index:
                update_block_data(block_index)
        elif option == 5:
            check_blockchain_integrity()
        elif option == 11:
            break
        else:
            print("Your in put is Invalid! Pleasse Input again")        
    print("\033[91m")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("\033[0m")
