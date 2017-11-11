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
        
    def hash(self, string):
        return sum(map(ord, string)) % self.size
        
    def rehash(self, j, firstHV):
        return (firstHV + j) % self.size
        
    def resize(self):
        pass
        
    def push(self, key, data):
        firstHV = self.hash(key)
        i = firstHV
        j = 0
        while self.table[i]:
            i = self.rehash(j, firstHV)
            j += 1

        self.table[i] = (key, data)

    def __setitem__(self, key, data):
        self.push(key, data)    
    
    def printTable(self):
        s = 'table size : {}, total : {}\n'.format(self.size, self.total)
        for i, j in enumerate(self.table):
            s += '{} : {}\n'.format(i, j)
        return s

    def __str__(self):
        return self.printTable()
    
    def get(self, key):
        firstHV = self.hash(key)
        i = firstHV
        j = 0
        while self.table[i][0] != key:
            i = self.rehash(j, firstHV)
            j += 1

        return self.table[i]
    
    def __getitem__(self, key):
        return self.get(key)
        
    def __iter__(self):
        for i in self.table:
            yield i

if __name__ == "__main__":
    h = HashTable()

    with open('input.txt', 'r') as f:
        for l in f:
            l = l.split()
            key = l[0]
            data = l[1]

            h[key] = data

    print(h)
    for i in h:
        if i:
            key = i[0]
            print('search ', i, ' found ', h[key])
