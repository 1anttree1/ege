from itertools import *
a = []
b = permutations('0123456789ABCDEF', r= 4)
for i in b:
    a.append(list(i))
h = 0
for i in a:
    if ((i.count("1") + i.count("3") + i.count("5") + i.count("7") + i.count("9")\
            + i.count("B") + i.count("D") + i.count("F")) == 2) and i[0] != "0":
        sumnch = i.count("1") + (3*i.count("3")) + 5*i.count("5") + 7*i.count("7") + 9*i.count("9")\
            + 11*i.count("B") + 13*i.count("D") + 15*i.count("F")
        sumch = 2*i.count("2") + 4*i.count("4") + 6*i.count("6") + 8*i.count("8")\
            + 10*i.count("A") + 12*i.count("C") + 14*i.count("E")
        if sumch == sumnch:
            h +=1
            print(i, sumch, sumnch)
print(h)
