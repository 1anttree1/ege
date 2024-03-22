from itertools import *
a = product('АИМРЯ', repeat = 4)
s = [''.join(i) for i in a]
for i in range(len(s)):
    if s[i] == 'АРИЯ': print(i+1)