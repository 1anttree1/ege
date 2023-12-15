from itertools import *

n = product('012345678', repeat=5)
a = []
for i in n:
    a.append(list(i))
h = 0
for i in a:
    if i.count('2') == 2 and i[0] != "0":
        for j in range(1, 3):
            if i[j] == "2" and i[j - 1] not in "1357" or i[j + 1] not in '1357':
                h += 1
print(h)
