class knapsack:
    def __init__(self, name, value, limit_money=None, weight=None, limit_weight=None):
        self.limit_money = limit_money
        self.limit_weight = limit_weight
        self.name = name
        self.value = value
        self.weight = weight

        self.n = len(value)
        self.sack = [-1]*self.n

    def __str__(self):
        s = ""
        for i in range(self.n):
            if self.sack[i] != -1:
                s += self.name[self.sack[i]] + ' ' + str(self.value[self.sack[i]]) + ', '
        return s
    
    def pick(self, i, j, m):
        if j < self.n:
            p = value[j]
            if m < p:
                self.pick(i, j+1, m)
            else:
                m -= p
                self.sack[i] = j
                if m == 0:
                    print(self, i)
                else:
                    self.pick(i+1, j+1, m)
                self.pick(i, j+1, m+p)

    def main(self):
        self.pick(0, 0, self.limit_money)

if __name__ == "__main__":
    name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk','cookie']
    value = [20, 10, 5, 5, 3, 2, 20, 10]
    limit_money = 20

    n = len(value)
    weight = [1]*n
    limit_weight = n
    
    k = knapsack(name, value, limit_money, weight, limit_weight)
    k.main()
