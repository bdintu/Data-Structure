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
        
def remove(r, d):
    if r:
        if d < r.d:
            r.l = remove(r.l, d)
        elif d > r.d:
            r.r = remove(r.r, d)
        else:
            if not r.l:
                return r.r
            elif not r.r:
                return r.l
            else:
                s = r.r
                while s.l:
                    s = s.l
                r.d = s.d
                r.r = remove(r.r, s.d)
        return r
        
def inOrder(r):
    if r:
        inOrder(r.l)
        print(r, end=' ')
        inOrder(r.r)
    
def printSideWay(r, l=0):
    if r:
        printSideWay(r.r, l+1)
        print(' '*3*l, r)
        printSideWay(r.l, l+1)
        
def height(r):
    if r:
        return max(height(r.l)+1, height(r.r)+1)
    else:
        return -1
        
def path(r, d):
    if r:
        print(r, end=' ')
        
        if d < r.d:
            path(r.l, d)
        elif d > r.d:
            path(r.r, d)
        
def search(r, d):
    if r:
        if d < r.d:
            return search(r.l, d)
        elif d > r.d:
            return search(r.r, d)
        else:
            return r
            
def depth(r, d):
    if r:
        if d < r.d:
            return depth(r.l, d) + 1
        elif d > r.d:
            return depth(r.r, d) + 1
        else:
            return 0
            
def bfs(r):
    s = [r]
    while(s):
        r = s.pop(0)
        print(r ,end=' ')
        if r.l:
            s.append(r.l)
        if r.r:
            s.append(r.r)

l = [14,4,9,7,15,3,18,16,20,5,16]
print('intput: ',l)

r = None

for i in l:
    r = add(r, i)

print('inorder:', end = ' ')
inOrder(r)
print()

print('printSideWay:')
printSideWay(r)

print('height of ', r, '=',  height(r));

d = 16
print('path:', d, '=', end = ' ')
path(r, d)
print()

t = search(r, d)
print(t)

print('depth of node data ', d, '=', depth(r, d))

print('bfs:', end = ' ')
bfs(r)
print()

remove(r, 16)
remove(r, 9)
remove(r, 18)
printSideWay(r)
