import transection as tx
import blockchain as bc
import data as d

def title_deed_data_input(tx_number):
    title_deed_number = str(input("\t\033[92mโฉนดที่ดินเลขที่:\033[0m "))
    data_time = str(input("\t\033[92mวัน-เวลาที่ออก:\033[0m "))
    parcel_number =str(input("\t\033[92mเลขที่ดิน:\033[0m "))
    near_parcel_number =str(input("\t\033[92mเลขที่ดินใกล้เคียง:\033[0m "))
    owner = str(input("\t\033[92mเจ้าของ:\033[0m "))
    subdistrict_name = str(input("\t\033[92mตำบล:\033[0m "))
    district = str(input("\t\033[92mอำเภอ:\033[0m "))
    province = str(input("\t\033[92mจังหวัด:\033[0m "))
    estimated_area_of_land = str(input("\t\033[92mที่ดินแปลงนี้มีเนื้อที่ประมาณ:\033[0m "))
    drafter = str(input("\t\033[92mผู้เขียนแผนที่:\033[0m "))
    map_investigator =str(input("\t\033[92mผู้ตรวจแผนที่:\033[0m "))
    title_deed = d.Title_Deed(title_deed_number, data_time, parcel_number, near_parcel_number, owner, subdistrict_name, district, province, estimated_area_of_land, drafter,  map_investigator)
    return tx.Transaction(tx_number, title_deed)

def print_title_deed_data(transaction):
    details = ['title_deed_number', 'data_time', 'parcel_number', 'near_parcel_number', 'owner', 'subdistrict_name', 'district', 'province', 'estimated_area_of_land', 'drafter', 'map_investigator']
    for detail in details:
        print(f"\t\033[92m{detail.capitalize():<30}\033[0m{getattr(transaction.title_deed, detail)}")

def show_block_data(block):
    if block:
        print(f"Block index: {block.index}")
        print(f"Previous block hash: {block.previous_hash}")
        print("Total transactions:", block.txs_count())
        print("Block data:")
        if block.index == 0:
            print(f"\t{block.data}")
        else:
            for transaction in block.data:
                print("\033[94m")
                print(f"transaction number : {transaction.index}")
                print("\033[0m")
                print_title_deed_data(transaction)
        print(f"Block hash: {block.hash}")
    else:
        print(f"No block found with index: {block.index}")

def write_a_block():
    temp = 0
    tx_number = 0
    transaction = []
    transactions = []
    option_type = ["C", "W", "c", "w"]
    while True:
        block_number = blockchain.block_count()
        if temp == 0:
            print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Block#{block_number + 1}")
            print(f"Input data to Transection NO.{tx_number} : ")
            transaction = title_deed_data_input(tx_number)
            transactions.append(transaction)
            print("Transaction created: ", transaction.hash)
            tx_number += 1
            temp = 1
        elif temp == 11:
            print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Block#{block_number} created")
            break
        else:
            while True:
                print("----------------------------------------------------------------------------\033[93m")
                option = str(input("Type (C) create next d. or (W) exit [write a block] (C/W)?: "))
                print("\033[0m----------------------------------------------------------------------------")
                if option in option_type:
                    if option == "C" or option == "c":
                        temp = 0
                    else:
                        blockchain.add_block(transactions)
                        temp = 11
                    break
                else:
                    print("Invalid Input! Please Input again")
def update_block_data(block_index):
    temp = 0
    tx_number = 0
    transactions = []
    option_type = ["C", "W", "c", "w"]
    while True:
        if temp == 0:
            block_number = blockchain.block_count()
            print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Block#{block_number}")
            print(f"Input data to Transection NO.{tx_number} : ")
            transaction = title_deed_data_input(tx_number)
            transactions.append(transaction)
            tx_number += 1
            temp = 1
        elif temp == 11:
            print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Block#{block_number} updated")
            break
        else:
            while True:
                print("----------------------------------------------------------------")
                option = str(input("Type (C) create next d. or (W) exit [write a block] (C/W)?: "))
                if option in option_type:
                    if option == "C" or option == "c":
                        temp = 0
                    else:
                        blockchain.update_block_data(block_index, transactions)
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
            print(f"Blockchain integrity compromised at block {i - 1}")
            print("\033[0m")
            return 12
    print("\033[94m"+"Blockchain integrity intact."+"\033[0m")


# create a new blockchain
blockchain = bc.Blockchain()

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
    print("3. find data")
    print("4. Update date in block")
    print("5. Check block integrity")
    print("\033[0m")
    print("\033[91m"+"11. to exit"+"\033[0m")
    print("\n")
    option = int(input("=> "))
    if option:
        if option == 1:
            write_a_block()
        elif option == 2:
            print("Select read option")
            print("1. list all block and data")
            print("2. select block to list data")
            s_option = int(input("=> "))
            if s_option == 1:
                for i in range(0, blockchain.block_count()):
                    block = blockchain.selectBlock(i)
                    print("\n============================================================== BLOCK #" + str(i))
                    show_block_data(block)
                    print("============================================================== BLOCK #" + str(i) + "\n")
            elif s_option == 2:
                block_num = int(input("Input Block number=> "))
                block = blockchain.selectBlock(block_num)
                print("\n============================================================== BLOCK #" + str(block_num))
                show_block_data(block)
                print("============================================================== BLOCK #" + str(block_num) + "\n")
        elif option == 3:
            name_to_find = str(input("Input you name=> "))
            selected_txs = blockchain.get_transactions_by_owner_name(name_to_find)
            print(f"Transactions for {name_to_find}:")
            print("Found: ", len(selected_txs), " transactions")
            if len(selected_txs) != 0:
                for transaction in selected_txs:
                    get_block_By_TxID = blockchain.get_block_by_tx_hash(transaction.hash)
                    print("\n============================================================== BLOCK #" + str(get_block_By_TxID))
                    print(f"Transaction#{transaction.index}")
                    print_title_deed_data(transaction)
                    print(f"Transaction hash: {transaction.hash}")
                    print("============================================================== BLOCK #" + str(get_block_By_TxID) + "\n")
            else:
                print(f"Not found owner name: {name_to_find}")
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
