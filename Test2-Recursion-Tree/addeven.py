def addEven(l, i, j):
	if i<= j:
		if l[i]%2 == 0:
			return addEven(l, i+1, j) + l[i]
		else:
			return addEven(l, i+1, j)
	else:
		return 0

l = [0, 1, 2, 3, 4, 5]
print(addEven(l, 0, 5))
