def work(n):
    if n == 1:
        print("do work ", n)
    else:
        work(n-1)
        print("do work ", n)

def printNdown(n):
    if n:
        print(n, end=' ')
        printNdown(n-1)

def printToN(n):
    if n:
        printToN(n-1)
        print(n, end=' ')

def sumToN(n):
    if n == 1:
        return 1
    else:
        return n + sumToN(n-1)

def printForw(l, i):
    if i < len(l):
        print(l[i], end=' ')
        printForw(l, i+1)

def printBack(l, i):
    if i < len(l):
        printBack(l, i+1)
        print(l[i], end=' ')

def App(l, n):
    if n:
        App(l, n-1)
        l.append(n)

def AppB(l, n):
    if n:
        l.append(n)
        AppB(l, n-1)

class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(h):
    if h:
        print(h.data, end = ' ')
        printList(h.next)

def createL(h, n):
    if n:
        t = node(n, h)
        t = createL(t, n-1)
        return t
    else:
        return h

def createLfromlist(h, l, n):
    if n:
        t = node(l[n-1], h)
        t = createLfromlist(t, l, n-1)
        return t
    else:
        return h

if __name__ == "__main__":
    n = 5
    work(n)
    printNdown(n)
    print()
    printToN(n)
    print()
    print(sumToN(n))

    l = [1, 2, 3, 4, 5]
    printForw(l, 0)
    print()
    printBack(l, 0)
    print()

    l = []
    App(l, n)
    print(l)

    l = []
    AppB(l, n)
    print(l)
    
    h = createL(None, n)
    printList(h)
    print()

    l = [1, 2, 3, 4, 5]
    n = len(l)
    h = createLfromlist(None, l, n)
    printList(h)
