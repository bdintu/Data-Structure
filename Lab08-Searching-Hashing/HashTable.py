from prime import isPrime

class rec:

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        return str((self.key, self.data))

class HashTable:

    def __init__(self):
        self.size = 11
        self.total = 0
        self.table = [None] * self.size

    def hash(self, string):
        return sum(map(ord, string)) % self.size

    def hash2(self, string):
        sum = 0
        for i in string:
            sum = sum << 5 + ord(i)
        return sum % self.size

    # linear probing
    def rehash(self, j, firstHV):
        return (firstHV + j) % self.size

    # quadratic probing
    def rehash2(self, j, firstHV):
        return (firstHV + j * j) % self.size

    def resize(self):
        oldSize = self.size
        oldTable = self.table

        self.size += 1
        while not isPrime(self.size):
            self.size += 1

        print ('resize from ', oldSize, ' to ', self.size)

        self.table = [None] * self.size
        self.total = 0

        for i in oldTable:
            if i:
                self.put(i.key, i.data)

    def put(self, key, data):
        if self.total / self.size >= 0.5:
            self.resize()

        firstHV = self.hash(key)
        print ('puting ', data, key)
        i = firstHV
        j = 1
        while self.table[i]:
            i = self.rehash(j, firstHV)
            print ('colission ', j, ' at ', i)
            j += 1

        self.total += 1
        self.table[i] = rec(key, data)

    def __setitem__(self, key, data):
        self.put(key, data)

    def printTable(self):
        s = 'table size : {}, total : {}\n'.format(self.size,
                self.total)
        for (i, j) in enumerate(self.table):
            if j:
                s += '{} : {}\n'.format(i, j)
        return s

    def __str__(self):
        return self.printTable()

    def get(self, key):
        firstHV = self.hash(key)
        i = firstHV
        j = 1
        while self.table[i].key != key:
            i = self.rehash(j, firstHV)
            j += 1

        return self.table[i]

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        for i in self.table:
            yield i

if __name__ == '__main__':
    h = HashTable()

    with open('input.txt', 'r') as f:
        for l in f:
            l = l.split()
            key = l[0]
            data = l[1]

            h[key] = data

    print (h)
    for i in h:
        if i:
            print ('search ', i, ' found ', h[i.key])

    h.resize()
    print (h)
			
