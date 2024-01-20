from itertools import *
h = 0
a = product('0123', repeat=3)
f = [''.join(i) for i in a]
for i in f:
    if i[0]>i[1]>i[2]:
        h += 1
print(h)