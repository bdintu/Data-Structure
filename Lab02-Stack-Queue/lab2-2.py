from stack import Stack

class ParenthesisMatching:
    def __init__(self, str):
        self.open = ['{', '[', '(']
        self.close = ['}', '}', ')']

        self.s = Stack()
        self.error = False
        self.str = str

    def match(self, open, close):
        return self.open.index(open) == self.close.index(close)

    def main(self):
        #what is that
        self.s.items = []
        for i in self.str:
            if i in self.open:
                self.s.push(i)
            elif i in self.close:
                if self.s.empty():
                    self.error = True
                else:
                    open = self.s.pop()
                    if not self.match(open, i):
                        self.error = True

    def __str__(self):
        if self.error:
            return "MISMATCH"
        elif not self.s.empty():
            return "MISMATCH open paren. exceed"
        else:
            return "MATCH" 

if __name__=="__main__":

	str = [ "s1 = ( a+b-c *[d+e]/{f*(g+h) }" ,
	        "s2 = [ ( a+b-c }*[d+e]/{f*(g+h) }" ,
	        "s3 = ( 3 + 2 ) / { 4**5 }" ]

	for i in str:
		p = ParenthesisMatching(i)
		p.main()
		print(p)
