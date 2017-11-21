from random import shuffle
#from prime import getPrime

def bubble(l):
	for i in range(len(l)):

		isSwap = False

		for j in range(len(l) -2, i-1, -1):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
				isSwap = True

		if not isSwap:
			break

def selection(l):
	for i in range(len(l)):

		min = l[i]
		min_index = i

		for j in range(i+1, len(l)):
			if min > l[j]:
				min = l[j]
				min_index = j
		
		l[i], l[min_index] = l[min_index], l[i]
		
def insertion(l):
	for i in range(1, len(l)):
		
		insert = l[i]
		
		for j in range(i, -1, -1):
			if insert < l[j-1] and j > 0:
				l[j] = l[j-1]
			else:
				l[j] = insert
				break

def shell(l, gaps):
	for gap in gaps:
		for i in range(gap, len(l)):

			insert = l[i]
			
			for j in range(i, -1, -gap):
				if insert < l[j-gap] and j >= gap:
					l[j] = l[j-gap]
				else:
					l[j] = insert
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

gaps = [3, 1]
shuffle(l)
print("l:", l)
shell(l, gaps)
print("shell:", l)
print()
