good = [20,10,5,5,3,2,20,10]
name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk','cookie']

def printSack(sack, last):
    for i in range(last+1):
        print(name[sack[i]],good[sack[i]], end = ' ')
    print()
    
def pick(sack, M, gi, si):
    if gi>-1:
        if M < good[gi]:
            pick(sack, M, gi-1, si)
        else:
            M -= good[gi]
            sack[si] = gi
            if M == 0:
                printSack(sack, si)
            else:
                pick(sack, M, gi-1, si+1)
            pick(sack, M+good[gi], gi-1, si)

N = len(good)
sack = [-1]*N
M = 20

pick(sack, M, N-1, 0)
