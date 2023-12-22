from cache import Cache
from memory import Memory 

initialization_value = 0
num_resister = 9

class Cpu:
    def __init__(self):
        self.cpu_counter =  initialization_value
        self.resister = [ [0] for i in range(num_resister)]
        self.cache = Cache()
        self.memory = Memory()
       # cache flag

    def set_counter(self, value = 1):
        self.cpu_counter += value

    def reset_counter(self):
        self.cpu_counter = initialization_value

    def get_num_counter(self):
        return self.cpu_counter

    def reset_resister(self):
        for i in range(len(self.resister)):
            self.resister[i] = 0

# review write and replace policies, addresses are bins    
    def search_cache(self, address):
        self.cache.search_value(address)

    def write_cache(self, address, value):
        self.cache.write_cache(address, value)

    def search_memory(self, address):
        self.memory.search_value(address)

    def write_memory(self, address, value):
        self.cache.write_memory(address, value)

# orders at each instruction
    def add(self, rd, rs, rt):
        self.resister[rd] = self.resister[rs] + self.resister[rt]

    def addi(self, rd, rs, immediate):
        self.resister[rd] = self.resister[rs] + int(immediate)






# main parse function
    def parse_instruction(self, instruction):
        instruction_parsed = instruction.split(",")
        print("Reading instruction: " + instruction)
        self.increment_cpu_counter()
        if instruction_parsed[0] == ADD_INSTRUCTION_OPERATOR:
            self.add_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == ADD_I_INSTRUCTION_OPERATOR:
            self.add_i_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == JUMP_INSTRUCTION_OPERATOR:
            self.jump_instruction(instruction_parsed[1])
        if instruction_parsed[0] == CACHE_INSTRUCTION_OPERATOR:
            self.cache_instruction(instruction_parsed[1])

            