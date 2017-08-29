import re

from ordered_list import orderedList
from term import term

def paser(expres):
    terms = re.findall(r"[+-]?[\s]*[\d]+[\s]*n[\s]*[\d]+", expres)

    for i in range(len(terms)):
        terms[i] = terms[i].replace(' ','')
    return terms

def main():
    print("test term")
    t1 = term(1.2, 3.4)
    t2 = term(0.8, 3.4)
    t3 = t1 + t2

    print("t1 :", t1)
    print("t2 :", t2)
    print("t3 :", t3)

    print("test orderedList")
    a = orderedList()
    b = orderedList()
    
    for i in range(5, 0, -1):
        a.insert(term(i+2, i+3))
        b.insert(term(i, i+2))

    c = a + b

    print("a :", a)
    print("b :", b)
    print("c :", c)

if __name__ == "__main__":
    main()
