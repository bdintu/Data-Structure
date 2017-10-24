def mul(self, x, n):
    if n == 0:
        return 0
    elif n > 0:
        return x + self.mul(x, n-1)
    elif n < 0:
        return -x + self.mul(x, n+1)

print(mul(2, 0))
print(mul(2, 5))
print(mul(2, -5))
print(mul(-2, 5))
print(mul(-2, -5))
