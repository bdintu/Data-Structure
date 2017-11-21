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

def printSideWay(r, l=0):
	if r:
		printSideWay(r.r, l+1)
		print(' '*3*l, r)
		printSideWay(r.l, l+1)

def doubleMore(r, d):
	if r:
		if d < r.d:
			print(r, ' -> ', 2*r.d)
			r.d *= 2
		else:
			print(r)

		if d < r.d:
			doubleMore(r.l, d)
			doubleMore(r.r, d)

		if d > r.d:
			doubleMore(r.r, d)

l = [14,4,9,7,15,3,18,16,20,5,16]
r = None
for i in l:
	r = add(r, i)
printSideWay(r)
print()
doubleMore(r, 8)
print()
printSideWay(r)
