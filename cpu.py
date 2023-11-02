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
       
    def set_counter(self, value = 1):
        self.cpu_counter += value

    def reset_counter(self):
        self.cpu_counter = initialization_value

    def get_num_counter(self):
        return self.cpu_counter

    def reset_resister(self):
        for i in range(len(self.resister)):
            self.resister[i] = 0
    
    def search_cache(self, address):
        self.cache.search_value(address)

    def write_cache(self, address, value):
        self.cache.write_cache(address, value)

    def search_memory(self, address):
        self.memory.search_value(address)

    def write_memory(self, address, value):
        self.cache.write_memory(address, value)

