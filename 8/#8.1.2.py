from itertools import *
n = permutations('0234567', r = 5)
a = []
h = 0
for i in n:
    a.append(list(i))
for i in a:
    if i[0] != '0' and (((i[0] in '246') and (i[1] in '357') and (i[2] in '0246') and (i[3] in '357') and (i[4] in '0246'))\
                        or ((i[0] in '357') and (i[1] in '0246') and (i[2] in '357') and (i[3] in '0246') and (i[4] in '357'))):
        h += 1
print(h)