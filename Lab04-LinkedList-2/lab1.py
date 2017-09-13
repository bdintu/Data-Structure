from list import list
from node import node

def status(l):
    print("l       : ", l)
    print("size    : ", l.size)
    print("-"*10)
l = list()
for i in range(2, -1, -1):
    l.push_front(node(i))
for i in range(3, 10):
    l.push_back(node(i))

print("list  : ", l)
print("empty : ", l.empty())
print("size  : ", l.size)
print("front : ", l.front())
print("back  : ", l.back())


print("remove 0: ", l.remove(0))
print("remove 9: ", l.remove(9))
status(l)

item4 = l.find(4)
if item4:
    print("find 4 is", item4.data)
print("erase 1-4: ", l.erase(None, l.begin, item4))
status(l)

print("pop_front:", l.pop_front().data)
print("pop_back: ", l.pop_back().data)
status(l)

