from queue import Queue

q = Queue()

name = input()
for i in name:
    q.enQueue(i)
    print("enQueue : ", i)
    print(q.items)

print()
print("items : ", q.items)
print("size : ", q.size())
print("empty : ", q.empty())
print("full : ", q.full())
print("front : ",q.front())
print()

while not q.empty():
    print("deQueue : ", q.deQueue())
    print(q.items)
