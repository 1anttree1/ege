from itertools import *
s = product('0123456789', repeat = 6 )
list1 = [str(i) for i in s]
h = 0
for i in list1:
    count = 0
    if i.count('0'):
        count += 1
    if i.count('2'):
        count += 1
    if i.count('4'):
        count += 1
    if i.count('6'):
        count += 1
    if i.count('8'):
        count += 1
    if int(i[-3])%2 == 0 and count == 2:
        h += 1
print(h)

