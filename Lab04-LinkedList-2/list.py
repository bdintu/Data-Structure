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

    def __in__(self, item):
        return bool(self.search(item))

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
        tmp = self.end
        self.end = self.before(self.end)
        self.end.next = None
        self.size -= 1
        return tmp

    def insert(self, pos, item=None, begin=None, end=None):
        if pos != None:
            item.next = pos.next
            pos.next = item
        else:
            end.next = pos.next
            pos.next = begin

    def search(self, item):
        for i in self:
            if i == item:
                return i
        return None

    def before(self, item):
        for i in self:
            if i.next == item:
                return i
        return None

    def find(self, data):
        for i in self:
            if i.data == data:
                return i
        return None

    def erase(self, item=None, begin=None, end=None):
        if item != None:
            if item == self.begin:
                self.begin = self.begin.next
            elif item == self.end:
                self.end = self.before(item)
                self.end.next = None
            else:
                cur = self.before(item)
                cur.next = cur.next.next
            self.size -= 1

        else:
            if begin == self.begin:
                self.begin = end.next
            elif end == self.end:
                self.end = self.before(begin)
                self.end.next = None
            else:
                cur = self.before(begin)
                cur.next = end.next
            self.size -= size(begin, end)

    def remove(self, data):
        item = self.find(data)
        self.erase(item)

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
