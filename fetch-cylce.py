
opcode_dict = {
                }
pc=0  
op=0
add=0

class Accumulator:
  
    def __init__(self):
        self.summation = 0
        self.memory = {
            "939":"0",
            "940":"3",
            "941":"5",
            "942":"9",
            "943":"8",
            "944":"0",
            "945":"99"


            
           
            }  
    def load_from_memory(self, address):
        if address in self.memory:
            self.summation = int(self.memory[address])
            print(f"Loaded value {self.summation} from memory address {address}")
           
        else:
            print(f"Memory address {address} not found.")
            
    def store_to_memory(self, address):
        self.memory[address] = str(self.summation)
        print(f"Stored value {self.summation} at memory address {address}.")
    def get_opcode_dict(self):
        addr_opcode = int(input("Enter an opcode address (eg:300...): "))
        for key, value in self.memory.items():
            if value == "0":
                address_key = key
                break
        address = int(address_key)
        global pc        
        global op
        global add
        pc = addr_opcode
        address += 1
        while True:                
            valid_opcodes = {"ADD": "3", "SUB": "4", "CLEAR": 'A', "LOAD": "2", "STORE": "1"}
            opcode = input(f"Enter your opcode for address {addr_opcode} like (add-sub-load-store-clear...): ").upper()
            if opcode == "CLEAR":
                opcode_dict[addr_opcode] = f"{valid_opcodes[opcode]} {self.summation}"
               
                
            elif opcode in valid_opcodes:
                opcode_dict[addr_opcode] = f"{valid_opcodes[opcode]} {address}"
                op = valid_opcodes[opcode]
                add = address
            else:
                print(f"Invalid opcode: {opcode}. Please enter..ADD, SUB, CLEAR, LOAD, STORE")
                address = address
                continue  

            another_entry = input("Do you want to add another entry? (y/n): ").lower()
            address += 1
            addr_opcode += 1

            if another_entry != 'y':
                break
        print("***********************************************************************")  
        return opcode_dict

    def execute_opcodes(self):
        x=1
        pc1 = pc

        for address in sorted(opcode_dict.keys()):
            opcode_info = opcode_dict[address]
            operation, operand_address = opcode_info.split()
            operand_address = int(operand_address)            
            stored_value=float(self.memory.get(str(operand_address), 0))
            print("***********************************************************************")

            if operation == "3":                  

                print(f"Added value {self.summation} with memory address {operand_address}")

                self.summation += stored_value

            elif operation == "4":                
                print(f"subtracted value {self.summation} with memory address {operand_address}")
                self.summation -= stored_value

            elif operation == 'A':  
                print("Cleared.......")
                self.summation = 0
            elif operation == "2":  
                self.load_from_memory(str(operand_address))
            elif operation == "1":  
                self.store_to_memory(str(operand_address))
            else:
                print(f"Invalid opcode: {operation}")
            print(f"{x} fetch-execute cycle")
            print(f"Program counter value: {pc1}")
            x+=1
            pc1+=1
            print(f"Instruction register: {operation} {operand_address}")

            print(f"Accumulator value: {my_accumulator.summation}")

            print("Memory contents:")
            for addr, val in my_accumulator.memory.items():
             print(f"Address {addr}: Value {val}") 

my_accumulator = Accumulator()
user_opcode_dict =my_accumulator.get_opcode_dict()
print(" opcode dictionary:")
print(user_opcode_dict)

my_accumulator.execute_opcodes()
  

       