class mul:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def __str__(self):
        return "%2d*%2d = %3d"%(self.x, self.n, self.mul(self.x, self.n))

    def mul(self, x, n):
        if n==0:
            return 0
        elif n > 0:
            return x + self.mul(x, n-1)
        elif n < 0:
            return -x + self.mul(x, n+1)

if __name__ == "__main__":
    print(mul(2, 0))
    print(mul(2, 5))
    print(mul(2, -5))
    print(mul(-2, 5))
    print(mul(-2, -5))
