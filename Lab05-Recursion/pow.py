class pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def __str__(self):
        return "%2d^%2d = %3d"%(self.x, self.n, self.pow(self.x, self.n))

class pow_on(pow):
    def pow(self, x, n):
        if n == 0:
            return 1
        else:
            return x * self.pow(x, n-1)

class pow_ologn(pow):
    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        elif n%2 == 0:
            return self.pow(x*x, n//2)
        else:
            return x * self.pow(x*x, n//2)

if __name__ == "__main__":
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
