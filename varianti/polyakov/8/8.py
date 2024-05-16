from itertools import *
a = [''.join(i) for i in product('ьрплеа', repeat = 5)]
h = 0
for i in range(388):
    if a[i][-1] == 'ь' :
        h += 1
print(h)