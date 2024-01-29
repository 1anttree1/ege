from itertools import *
a = product('0123456', repeat=5)
s = [''.join(i) for i in a]
h = 0
for i in s:
    if i[0] == '4' and int(i[1]) % 2 == 0 and i.count('4') == 1:
        h += 1
    elif i[0] != '0' and i[1] == '4' and (int(i[0]) % 2 == 0 and int(i[2]) % 2 == 0) and i.count('4') == 1:
        h += 1
    elif i[0] != '0' and i[2] == '4' and int(i[1]) % 2 == 0 and int(i[3]) % 2 == 0 and i.count('4') == 1:
        h += 1
    elif i[0] != '0' and i[3] == '4' and int(i[2]) % 2 == 0 and int(i[4]) % 2 == 0 and i.count('4') == 1:
        h += 1
    elif i[0] != '0' and i[4] == '4' and int(i[3]) % 2 == 0 and i.count('4') == 1:
        h += 1

print(h)