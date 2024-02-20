from itertools import *
a = permutations('ИДИЛЛИЯ', r = 7)
s = [''.join(i) for i in a]
f = set()
for i in s:
    f.add(i)
print(len(f))

