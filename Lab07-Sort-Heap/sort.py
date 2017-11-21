from random import shuffle

def bubbleSort(l):
	for i in range(len(l)):

		isSwap = False

		for j in range(len(l) -2, i-1, -1):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
				isSwap = True

		if not isSwap:
			break

def selectionSort(l):
	for i in range(len(l)):

		min, min_index = l[i], i

		for j in range(i+1, len(l)):
			if min > l[j]:
				min = l[j]
				min_index = j
		
		l[i], l[min_index] = l[min_index], l[i]
		
def insertionSort(l):
	for i in range(1, len(l)):
		
		insert = l[i]
		
		for j in range(i, -1, -1):
			if insert < l[j-1] and j > 0:
				l[j] = l[j-1]
			else:
				l[j] = insert
				break

def shellSort(l, gaps):
	for gap in gaps:
		for i in range(gap, len(l)):

			insert = l[i]
			
			for j in range(i, -1, -gap):
				if insert < l[j-gap] and j >= gap:
					l[j] = l[j-gap]
				else:
					l[j] = insert
					break
				
def mergeSort(l, left, right):
	if left < right:
		mid = (left+right)//2

		mergeSort(l, left, mid)
		mergeSort(l, mid+1, right)
		merge(l, left, mid, right)

def merge(l, left, mid, right):
	i, j = left, mid + 1
	result = []
	
	while i <= mid and j <= right:
		if l[i] < l[j]:
			result.append(l[i])
			i += 1
		else:
			result.append(l[j])
			j += 1
			
	while i <= mid:
		result.append(l[i])
		i += 1
		
	while j <= right:
		result.append(l[j])
		j += 1
		
	i = left
	for j in result:
		l[i] = j
		i += 1
		
def quickSort(l, left, right):
	if left < right:
		pivot = quick(l, left, right)
		quickSort(l, left, pivot-1)
		quickSort(l, pivot+1, right)
		
def quick(l, left, right):
	pivot = l[left]
	i, j = left+1, right
	
	while i<j:
		
		while i < right and l[i] <= pivot:
			i += 1
		
		while j > left and l[j] >= pivot:
			j -= 1

		if i < j:
			l[i], l[j] = l[j], l[i]
			
	l[left], l[j] = l[j], l[left]
	
	return j

l = [i*i for i in range(1, 7)]

shuffle(l)
print("l:", l)
bubbleSort(l)
print("bubble:", l)
print()

shuffle(l)
print("l:", l)
selectionSort(l)
print("selection:", l)
print()

shuffle(l)
print("l:", l)
insertionSort(l)
print("insertion:", l)
print()

gaps = [19, 5, 1]
shuffle(l)
print("l:", l)
shellSort(l, gaps)
print("shell:", l)
print()

shuffle(l)
print("l:", l)
mergeSort(l, 0, len(l)-1)
print("merge:", l)
print()


shuffle(l)
print("l:", l)
quickSort(l, 0, len(l)-1)
print("quick:", l)
print()
