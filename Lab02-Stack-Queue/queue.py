class Queue:
    def __init__(self, items=[], max_size=100):
        self.items = items
        self.max_size = max_size

    def size(self):
        return len(self.items)

    def empty(self):
        return self.items == []

    def full(self):
        return self.size() == self.max_size

    def front(self):
        return self.items[0]

    def enQueue(self, element):
        self.items +=[element]

    def deQueue(self):
        return self.items.pop(0) 
