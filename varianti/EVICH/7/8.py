from itertools import *
a = permutations('0123456789', r = 6)
s = [''.join(i) for i in a]
sch = '02468'
snch = '13579'
h = 0
for i in s:
    ch = nch = 0
    if i[0] != '0' and i[-2:] == '26':
        for j in i:
            if j in sch:
                ch += 1
            if j in snch:
                nch += 1
        if ch == 3 or nch == 2:
            h += 1
print(h)


        