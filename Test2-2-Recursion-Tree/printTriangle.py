def printStar(n):
    if n:
        print('*', end='')
        printStar(n-1)
        
def printTriangle(n):
    if n:
        printStar(n)
        print()
        printTriangle(n-1)
        printStar(n)
        print()
        
printTriangle(5)
