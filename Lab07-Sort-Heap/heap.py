def print90(h):
    pass

def insert(h, d):
    pass

def deleteMin(h):
    pass

h = []
l = [68,65,32,24,26,21,19,13,16,14]
for i in l:
    insert(h, i)

print90(h)

for i in range(len(l)):
    deleteMin(h)
    
print90(h)
