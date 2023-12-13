from itertools import *
n = permutations("улей", r=4)
a = []
for i in n:
    a.append(list(i))
h = 0
for i in a:
    if (i[0] != "й") and (i[0] + i[1] != 'еу') and (i[1] + i[2] != 'еу') and (i[2] + i[3] != 'еу'):
        print(i)
        h += 1
print(h)