class Stack:
    def __init__(self, items=[], max=128):
        self.items = items
        self.max = max

    def __len__(self):
        return len(self.items)

    def __if__(self):
        return self.__len__() != 0

    def __str__(self):
        return str(self.items)

    def push(self, element):
        if len(self) < self.max:
            self.items += [element]

    def pop(self):
        if self:
            return self.items.pop()

    def peek(self):
        if self:
            return self.items[-1]

    def size(self):
        return self.__len__()

    def empty(self):
        return not self.__if__()

    def full(self):
        return self.__len__() == self.max

    def clear(self):
        self.items = []
