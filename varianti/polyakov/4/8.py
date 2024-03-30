from itertools import *
s = 'уа'
a = [''.join(i) for i in product('адуч', repeat = 5) if i[0] in s]
for i in range(len(a)):
    if a[i] == 'удача':
        print(i)
