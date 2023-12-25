from itertools import *
s = product('012345678', repeat=6)
list1 = [list(i) for i in s]
h = 0
print(len(list1))
for i in list1:
    if (int(i[-1])%2 == 0) and ((i.count('2') + i.count('4') + i.count('6') + i.count('8')) == 2) and (i[0] != '0'):
        h += 1


print(h)

