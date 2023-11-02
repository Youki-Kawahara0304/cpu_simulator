cache_size = 16

class Cache:
    def __init__(self):
        self.entries = [{} for i in range(cache_size)]
        self.place_to_replace = 0

    def refresh_cache(self):
        self.entries = [{} for i in range(cache_size)]

    def write_cache(self, address, value):
        for entry in self.entries:
            if entry == {}:
                entry.update({address: value})
                return
        self.entries[self.place_to_replace] = {address: value}
        self.place_to_replace += 1
        if self.place_to_replace == 16:
            self.place_to_replace = 0
    
    def search_value(self, address):
        for entry in self.entries:
            print(entry)
            if address in entry:
                return entry[address]
        return None



test = Cache()
for i in range(0, 33):
    test.write_cache(i, "test")    
print(test.search_value(33))