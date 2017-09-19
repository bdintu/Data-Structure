from stack import Stack

class InfixToPostfix:
    def __init__(self, infix):
        self.infix = infix

        self.postfix = []
        self.s = Stack()
        self.opt = {'*': 2,
                    '/': 2,
                    '%': 2,
                    '+': 1,
                    '-': 1,
                    '(': 0
                    }

    def main(self):
        for i in self.infix:
            if  i.isalpha() or i.isdigit():
                self.postfix += [i]
            elif i == '(':
                self.s.push(i)
            elif i == ')':
                while self.s.peek() != '(':
                    self.postfix += [self.s.pop()]
                self.s.pop()
            else:
                while self.s and self.opt[i] <= self.opt[ self.s.peek() ]:
                    self.postfix += [self.s.pop()]
                self.s.push(i)

        while self.s:
            self.postfix += [self.s.pop()]

    def __str__(self):
        return ''.join(self.postfix)

if __name__ == "__main__":
    infix = [   "a*b+c",
                "a+b*c",
                "a+b*c-d",
                "a+b*c-(d/e+f)*g"
            ]

    for i in infix:
        c = InfixToPostfix(i)
        c.main()
        print(c)
