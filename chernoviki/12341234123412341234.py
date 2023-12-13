from itertools import *
k = 1
for x in range(1,11 ):
    a = permutations('0123456789', r = x)
    list1 = []
    for i in a:
        list1.append(list(i))
    for i in list1:
        if i[0] != '0' and (i[-1] == '0' or i[-1] == '5'):
            k += 1
    print(k)
