def bsearchR(a, x ,l, h):
    if l > h:
        return -1

    mid = (l+h)//2
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        return bsearchR(a, x, mid+1, h)
    else:
        return bsearchR(a, x, l, mid-1)

def bsearchI(a ,x):
    low = 0
    hight = len(l) -1

    while low < hight:
        mid = (low+hight)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid +1
        else:
            hight = mid -1

    return -1

if __name__ == "__main__":
    l = [i for i in range(10)]
    x = 5
    print(bsearchR(l, x, 0, len(l)-1))
    print(bsearchI(l ,x))
