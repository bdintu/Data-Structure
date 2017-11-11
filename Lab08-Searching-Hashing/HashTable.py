#form prime import isPrime

class rec:
    def __init__(self, key, data):
        self.key = key
        self.data = data
    
    def __str__(self):
        return str((self.key,self.data))
        
class HashTable:
    def __init__(self):
        self.size = 11
        self.total = 0
        self.table = [None]*self.size
        
    def hash(string, tablesize):
        return sum(map(ord, string)) % tablesize
        
    def rehash(j, firstHV, tablesize):
        return (firstHV + j) % tablesize
        
    def resize(self):
        pass
        
    def push(self, key, data):
        pass
    
    def __setitem__(self, key, data):
        self.push(key, data)    
    
    def printTable(self):
        pass
    
    def get(self, key):
        pass
    
    def __getitem__(self, key):
        self.get(key)
        
if __name__ == "__main__":
    h = HashTable()
    with open('input.txt', 'r') as f:
        for l in f:
            l = l.split()
            key = l[0]
            data = l[1]

            h[key] = data
