from itertools import *
h = 1
for x in range(1, 5):
    n = permutations("0123456789", r=x)
    a = []
    for i in n:
         a.append(list(i))
    for i in a:
        if int("".join(i)) %5 ==0 and i[0] != "0" :
            h += 1
print(h)