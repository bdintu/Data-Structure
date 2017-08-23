from stack import Stack

class NarrowParkingLot():
    def __init__(self, max_size):
        self.s1 = Stack([], max_size)
        self.s2 = Stack([], max_size)

    def arrive(self, name):
        self.s1.push(name)

    def depart(self, name):
        if self.check_name and self.s1.peek() == name:
            return self.s1.pop()
        else:
            while self.s1.peek() != name:
                tmp = self.s1.pop()
                self.s2.push(tmp)
                print("pop ", tmp)
            tmp = self.s1.pop()
            while not self.s2.empty():
                tmp = self.s2.pop()
                self.s1.push(tmp)
                print("push ", tmp)
            return tmp

    def check_name(self, name):
        return name in self.s1.items

    def main(self, menu):
        if menu == "p":
            print("print soi = ", self.s1.items)
        elif menu == "a":
            name = input()
            if self.s1.full():
                 print("car ", name, " cannot arrive : SOL FULL")
            else:
                self.arrive(name)
                print("car ", name, " arrive \tspace left ", self.s1.max_size - self.s1.size())
        elif menu == "d":
            name = input()
            if self.s1.empty():
                print("car ", name, "cannot depart: soi empty")
            else:
                print("car 2 depart :")
                self.depart(name)
        else:
            print("menu error")

if __name__ == "__main__":
    p = NarrowParkingLot(4)
    
    c = ""
    while not c == "e":
        print("press a : arrive")
        print("press d : depart")
        print("press p : print soi")
        print("press e : exit")
        menu = input()
        p.main(menu)
