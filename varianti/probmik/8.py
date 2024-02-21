from itertools import *
a = product('ABC', repeat = 5)
s = [''.join(i) for i in a]
h = 0
for i in s:
    if i.count('A') == 1 and (i[0] == 'A' or i[-1] == 'A'):
        h += 1
print(h)