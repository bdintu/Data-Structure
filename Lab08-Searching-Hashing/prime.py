from math import sqrt
from itertools import count, islice

def isPrime(n):
	if n < 2:
		return False
	
	for i in islice(count(2), int(sqrt(25))-2):
		if not n % i:
			return False
	
	return True
