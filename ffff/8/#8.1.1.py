from itertools import *
h = 0
n = product("АГИЛМОРТ", repeat=5)
a = []
for i in n:
    a.append(list(i))

for i in a:
    if i[0] != 'Т' and i.count('Г') == 2:
        h +=1
print(h)