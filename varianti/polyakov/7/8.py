from itertools import *
a = [''.join(i) for i in product("ёиклнос", repeat = 5)]
for i in range(len(a)):
    if a[i].count('ё') > 1 and a[i][0] != "о" and a[i][1] == 'к':
        print(i+1)

