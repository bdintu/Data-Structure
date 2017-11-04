class node:
    def __init__(self, d, l=None, r=None, h=0):
        self.d = d
        self.l = l
        self.r = r
        self.h = h
    
    def __str__(self):
        return "{}:{}".format(self.d, self.h)
        
def addH(r, d):
    if not r:
        return node(d)
    else:
        if d < r.d:
            r.l = addH(r.l, d)
        else:
            r.r = addH(r.r, d)
            
        if r.l and r.r:
            r.h = max(r.l.h, r.r.h) + 1
        elif r.l:
            r.h = r.l.h + 1
        else:
            r.h = r.r.h + 1
            
        return r

def printSideWay(r, l=0):
	if r:
		printSideWay(r.r, l+1)
		print(' '*3*l, r)
		printSideWay(r.l, l+1)

l = [14,4,9,7,15,3,18,16,20,5,16]
r = None
for i in l:
	r = addH(r, i)
printSideWay(r)
