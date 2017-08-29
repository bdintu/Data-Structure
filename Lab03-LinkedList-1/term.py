class term:
    def __init__(self, coeffic=0, power=0):
        self.coeffic = coeffic
        self.power = power

    def __str__(self):
        return "%+fn^%f"%(self.coeffic, self.power)

    def __add__(self, rhs):
        if self == rhs:
            coeffic = self.coeffic + rhs.coeffic
            return term(coeffic, self.power)

    def __iadd__(self, rhs):
        return self.__add__(rhs)

    def __eq__(self, rhs):
        return self.power == rhs.power

    def __lt__(self, rhs):
        return self.power < rhs.power or (self.power == rhs.power and self.coeffic < rhs.coeffic)
