def factR(n):
    if n == 1:  
        return 1
    else:
        return n * factR(n-1)

def factI(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum

if __name__ == "__main__":
    print(factR(5))
    print(factI(5))
