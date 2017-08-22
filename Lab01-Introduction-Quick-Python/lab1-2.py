def multiples_of_3_and_5(n):
    sum = 0
    m = [3, 5]

    for i in m:
        for j in range(i, n, i):
            sum += j

    for i in range(15, n, 15):
        sum -= i

    return sum

print(multiples_of_3_and_5(10))
