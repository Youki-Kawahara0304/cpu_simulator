memory_size = 128

class Memory:
    def __init__(self):
        self.memory_bus = {}
        self.set_memory_bus()

    def set_memory_bus(self):
        for i in range(memory_size):
            self.memory_bus[i] = 0

    def write_memory(self, address, value):
        if self.memory_bus.get(address) is not None:
            self.memory_bus[address] = value
                
    def search_memory(self, address):
        if self.memory_bus.get(address) is not None:
            return self.memory_bus.get(address)
        return None
