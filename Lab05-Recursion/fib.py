def fibR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibR(n-1) + fibR(n-2)

def fibI(n):
    lo, hi = 0, 1
    for i in range(2, n+1):
        new = lo + hi
        lo = hi
        hi = new
    return new

if __name__ == "__main__":
    print(fibR(5))
    print(fibI(5))
