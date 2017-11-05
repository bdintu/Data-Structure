def p(i):
    return (i-1)//2
    
def cl(i):
    return i*2 +1
    
def cr(i):
    return i*2 +2
    
def print90(h, i=0, l=0):
    if i < len(h):
        print90(h, cr(i), l+1)
        print(' '*3*l, h[i])
        print90(h, cl(i), l+1) 

def insert(h, d):
    h.append(d)
    i = len(h)-1

    while h[i] < h[p(i)] and i!=0:
        h[i], h[p(i)] = h[p(i)], h[i]
        i = (i-1)//2

def deleteMin(h):
    tmp = h[0]
    s = len(h) -1
    i = 0
    
    while cl(i) < s:
        if h[cl(i)] < h[cr(i)]:
            h[i] = h[cl(i)]
            i = cl(i)
        else:
            h[i] = h[cr(i)]
            i = cr(i)

    h[i] = h[s]
    h[s] = tmp

h = []
l = [68,65,32,24,26,21,19,13,16,14]
for i in l:
    print("insert:", i)
    insert(h, i)
    print("heap:", h)
    print("heap:")
    print90(h)    

print("heap:", h)
print("heap:")
print90(h)

for i in range(len(l)):
    print("deleteMin=", h[0], "FindPlaceFor", h[len(l)-1])
    deleteMin(h)
    print("heap:", h)
    print("heap:")
    print90(h)
