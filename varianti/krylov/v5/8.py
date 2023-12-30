from itertools import *
a = product('01234567', repeat = 5)
list1 = [list(i) for i in a]
count = 0
for i in list1:
    h = 0
    if i.count('4') != 2 or i[0] == '0':
        continue
    if i[0] == '4' and i[1] in '1357':
            h += 1
    if i[-1] == '4' and i[-2] in '1357':
            h += 1
    for j in range(1, len(i) - 1):
        if i[j] == '4' and (i[j-1] in '1357' or i[j+1] in '1357'):
            h += 1
    if h == 0:
        count += 1
print(count)