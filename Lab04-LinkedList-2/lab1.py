from list import list
from node import node

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

tmp = l.find(2)
if tmp:
    print("find 2 is", tmp.data)

print("remove 0: ", l.remove(0))
print("remove 5: ", l.remove(5))
print("remove 9: ", l.remove(9))
print("pop_front:", l.pop_front().data)
print("pop_back: ", l.pop_back().data)
print("l       : ", l)
print("size    : ", l.size)
