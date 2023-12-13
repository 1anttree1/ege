from itertools import *
n = product("ЕГЭ", repeat=5)
a = []
for i in n:
    a.append(list(i))
h = 0
for i in a:
    if i[0] == 'Е' or i[0] == 'Э':
        h +=1
print(h)
