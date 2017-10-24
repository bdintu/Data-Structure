def pow_on(self, x, n):
    if n == 0:
        return 1
    else:
        return x * self.pow(x, n-1)

def pow_ologn(self, x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    elif n%2 == 0:
        return self.pow(x*x, n//2)
    else:
        return x * self.pow(x*x, n//2)
    
print(pow_on(2, 0))
print(pow_on(2, 3))
print(pow_on(-2, 3))
print(pow_on(2, 4))
print(pow_on(-2, 4))

print(pow_ologn(2, 0))
print(pow_ologn(2, 3))
print(pow_ologn(-2, 3))
print(pow_ologn(2, 4))
print(pow_ologn(-2, 4))
