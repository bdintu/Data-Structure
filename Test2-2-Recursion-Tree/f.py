class node:
    def __init__(self, d, l=None, r=None):
        self.d = d
        self.l = l
        self.r = r
    
    def __str__(self):
        return str(self.d)
        
def add(r, d):
    if not r:
        return node(d)
    else:
        if d < r.d:
            r.l = add(r.l, d)
        else:
            r.r = add(r.r, d)

        return r
        
def inOrder(r):
    if r:
        inOrder(r.l)
        print(r, end=' ')
        inOrder(r.r)

def g(r, n):
    if r:
        g(r.l, n)
        f = 0
        if n >= r.d:
            if r.r:
                f = g(r.r, n) + 1
        return f

def printSideWay(r, l=0):
	if r:
		printSideWay(r.r, l+1)
		print(' '*3*l, r)
		printSideWay(r.l, l+1)

l = [14,4,9,7,15,3,18,16,20,5,17]
r = None
for i in l:
	r = add(r, i)
	
print('inOrder : ')
inOrder(r)
print()

printSideWay(r)
print()

n = 4
print("{}:{}".format(n, g(r, n)))
