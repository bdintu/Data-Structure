from node import node
from list import list

class scramble:
    def __init__(self):
        self.l = list()

    def __str__(self):
        return str(self.l)

    def _split(self, p):
        n = int(p*self.l.size/100)
        i = 0
        for it in self.l:
            i = i+1
            if i == n:
                return it

    def bottomUp(self, p):
        if p == 0:
            return

        begin = self.l.begin
        end = self._split(p)
        self.l.erase(None, begin, end)
        self.l.push_back(None, begin, end)
        end.next = None

    def riffle(self, p):
        if p == 0:
            return

        begin = self._split(p)
        i = self.l.begin
        j = begin.next
        begin.next = None

        while i!=None and j!=None:
            tmp = j.next
            j.next = i.next
            i.next = j
            i = i.next.next
            j = tmp
       
        if j != None:
            i = j

    def deRiffle(self, p):
        p = self.l.size - (p/100*self.l.size)
        n = 0

    def deBottomUp(self, p):
        self.bottomUp(100-p)

if __name__ == "__main__":
    s = scramble()
    for i in range(1,11):
        s.l.push_back(node(i))
    print("l : ", s)

    s.bottomUp(30)
    print("bottomUp 30% : ", s)

    s.riffle(60)
    print("riffle 60%   : ", s)

    s.deRiffle(60)
    print("deRiffle 60% : ", s)

    s.deBottomUp(30)
    print("deBottonUp 30:", s)
