from node import node
from list import list

class scramble:
    def __init__(self):
        self.l = list()

    def __str__(self):
        return str(self.l)

    def split(self, p):
        n = int(p*self.l.size/100)
        i = 0
        for it in self.l:
            i = i+1
            if i == n:
                return it

    def bottomUp(self, p):
        if p == 0:
            return
        last = self.split(p)
        self.l.end.next = self.l.begin
        self.l.begin = last.next
        last.next = None

    def riffle(self, p):
        if p == 0:
            return
        start = self.split(p)
        i = self.l.begin
        j = start.next
        start.next = None
        while i!=None and j!=None:
            tmp_i = i.next
            tmp_j = j.next

            j.next = i.next
            i.next = j
            tmp = i.next
            i = tmp_i
            j = tmp_j
       
        if i != None:
            tmp.next = i
        else:
            tmp.next = j
        

    def deRiffle(self, percent):
        pass

    def deBottomUp(self, percent):
        pass

if __name__ == "__main__":
    s = scramble()
    for i in range(1,11):
        s.l.push_back(node(i))
    print("l : ", s)

    s.bottomUp(30)
    print("bottomUp 30% : ", s)

    s.riffle(60)
    print("riffle 60%   : ", s)
