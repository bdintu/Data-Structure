def integer_right_triangles(p):
    l = [   [3, 4, 5],
            [5, 12, 13],
            [7, 24, 25],
            [8, 15, 17],
            [9, 40, 41],
            [11, 60, 61],
            [12, 35, 37],
            [13, 84, 85],
            [20, 21, 29]
        ]

    for i in l:
        s = sum(i)
        if p%s == 0:
            k = p/s
            print(k*i[0], k*i[1], k*i[2])

integer_right_triangles(60)
