from itertools import *
n = product("012345678", repeat=5)
a = []
w = ["12", '21', '23', '32', '25', '52', '27', '72']
for i in n:
    a.append(list(i))
h = 0
for i in a:
    j = ''.join(i)
    if i.count("3") == 2 and i[0] != '0' and (j[0]+j[1] not in w) and (j[1]+j[2] not in w) and (j[2]+j[3] not in w) and (j[3]+j[4] not in w):
        h += 1
        print(i)
print(h)