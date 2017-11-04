from random import shuffle

def bubble(l):
    for i in range(len(l)-1):
        isSwap = False
        
        for j in range(len(l)-2, i-1, -1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                isSwap = True

        if not isSwap:
            break;
            
def selection(l):
    for i in range(len(l)-1):
        min = l[i]
        min_i = i
        for j in range(i+1, len(l)):
            if l[j] < min:
                min = l[j]
                min_i = j
                
        l[i], l[min_i] = l[min_i], l[i]
        
def insertion(l):
    for i in range(len(l)):
        select = l[i]
        for j in range(i, -1, -1):
            if select < l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = select
                break

l = [i*i for i in range(1, 6)]

shuffle(l)
print("l:", l)
bubble(l)
print("bubble:", l)
print()

shuffle(l)
print("l:", l)
selection(l)
print("selection:", l)
print()

shuffle(l)
print("l:", l)
insertion(l)
print("insertion:", l)
print()
