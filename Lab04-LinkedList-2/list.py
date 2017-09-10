class list:
    def __init__(self):
        self.begin = None
        self.end = None
        self.size = 0

    def __iter__(self):
        cur = self.begin
        while(cur != None):
            yield cur
            cur = cur.next
   
    def __len__(self):
        return self.size

    def __if__(self):
        return self.empty()

    def __str__(self):
        s = ""
        for i in self:
            s += str(i.data) + " -> "
        return s
 
    def empty(self):
        return self.begin == None

    def clear(self):
        self.begin = None

    def front(self):
        return self.begin.data

    def back(self):
        return self.end.data

    def push_front(self, item=None, begin=None, end=None):
        if item != None:
            if self.empty():
                self.end = item
            else:
                item.next = self.begin
            self.begin = item
            self.size += 1

        elif begin!=None and end!=None:
            if self.empty():
                self.end = end
            else:
                end.next = self.begin
            self.begin = begin
            self.size += size(begin, end)

    def push_back(self, item=None, begin=None, end=None):
        if item != None:
            if self.empty():
                self.begin = item
            else:
                self.end.next = item
            self.end = item
            self.size += 1

        else:
            if self.empty():
                self.begin = begin
            else:
                self.end.next = begin
            self.end = end
            self.size += size(begin, end)

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

    def erase(self, begin, end):
        if begin == self.begin:
            self.begin = end.next
        elif end == self.end:
            self.end = self.before(begin.data)
        else:    
            cur = self.begin
            while(cur.next != begin):
                print(cur.data, begin.data)
                cur = cur.next
            cur.next = end.next

        self.size -= size(begin, end)

    def remove(self, data):
        if self.begin.data == data:
            self.pop_front()
        else:
            cur = self.before(data)
            if cur != None:
                if cur.next.next == None:
                    self.end = cur
                cur.next = cur.next.next

def travel(begin, end):
    cur = begin
    while(cur != None):
        yield cur
        if cur == end:
            return
        cur = cur.next

def size(begin, end):
    n = 0
    for i in travel(begin, end):
        n += 1
    return n
