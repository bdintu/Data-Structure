class list:
    def __init__(self):
        self.begin = None
        self.end = None
        self.size = 0

    def __str__(self):
        s = ""
        for i in self:
            s += str(i.data) + " -> "
        return s

    def __iter__(self):
        cur = self.begin
        while(cur != None):
            yield cur
            cur = cur.next
    
    def __len__(self):
        return self.size

    def empty(self):
        return self.begin == None

    def clear(self):
        self.begin = None

    def front(self):
        return self.begin.data

    def back(self):
        return self.end.data

    def push_front(self, item):
        if self.begin == None:
            self.end = item
            item.next = None
        else:
            item.next = self.begin
        self.begin = item
        self.size += 1

    def push_back(self, item):
        if self.begin == None:
            self.begin = item
        else:
            self.end.next = item
        self.end = item
        item.next = None
        self.size += 1

    def pop_front(self):
        tmp = self.begin
        self.begin = self.begin.next
        self.size -= 1
        return tmp

    def pop_back(self):
        tmp =self.end
        cur = self.begin
        while(cur.next.next != None):
            cur = cur.next
        cur.next = None
        self.end = cur
        self.size -= 1
        return tmp

    def find(self, data):
        for i in self.travel():
            if i.data == data:
                return i
        return None

    def before(self, data):
        for i in self.travel():
            if i.next != None and i.next.data == data:
                return i
        return None

    def remove(self, data):
        if self.begin.data == data:
            self.pop_front()
        else:
            cur = self.before(data)
            if cur != None:
                if cur.next.next == None:
                    self.end = cur
                cur.next = cur.next.next
                self.size -= 1
