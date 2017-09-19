from stack import Stack
class PostfixEval:
    def __init__(self, postfix):
        self.postfix = postfix

        self.s = Stack()
        self.result = -1

    def __str__(self):
        return str(self.result)

    def main(self):
        for i in self.postfix:
            if i.isdigit():
                self.s.push(i)
            else:
                op1 = self.s.pop()
                op2 = self.s.pop()
                r = eval("%s%s%s"%(op1, i, op2))
                self.s.push(str(r))

        self.result = self.s.pop()

if __name__ == "__main__":
    p = PostfixEval("456*+")
    p.main()
    print(p)
