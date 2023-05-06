# hash table by Karl Poulson
# A hash table is like a python dictionary
# It asssigns a value to a unique space according to a hash function
# This value can be accessed via it's key, which can be some data type

class HashMap():
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def myHash(self, key):
        return hash(key) % self.size
        
    def put(self, key, value):
        key = self.myHash(key)
        self.table[key] = value

    def get(self, key):
        key = self.myHash(key)
        return self.table[key]

    def remove(self, key):
        key = self.myHash(key)
        self.table[key] = None

ht = HashMap(10)
ht.put("greet", "Hello there Mr Bond")
print(ht.get("greet"))
ht.remove("greet")
print(ht.get("greet"))
