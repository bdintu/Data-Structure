class Stack:
    def __init__(self, items=[], max_size=256):
        self.items = items
        self.max_size = max_size

    def push(self, element):
        self.items += [element]

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def empty(self):
        return self.items == []

    def full(self):
        return self.size() == self.max_size;
