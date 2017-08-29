class orderedList:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def insert(self, element):
        if self.empty():
            self.items = [element]
        else:
            for i in range(len(self)):
                if self.items[i] == element:
                    self.items[i] += element
                    return
                elif self.items[i] < element:
                    continue
                else:
                    break

            if self.items[i] < element: 
                self.items += [element]
            else:
                self.items.insert(i, element)


    def empty(self):
        return len(self)==0

    def __str__(self):
        tmp = ""
        for i in range(len(self)):
            tmp += str(self.items[i])
            tmp += ' '
        tmp += '\n'
        return tmp

    def __add__(self, rhs):
        tmp = orderedList()
        for i in self.items + rhs.items:
            tmp.insert(i)

        return tmp
