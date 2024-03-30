from itertools import *
a = [''.join(i) for i in product('агилморт', repeat = 5)]
for i in range(len(a)):
    if a[i][0] != "т" and a[i].count('г') == 2 and (i+1) % 2 == 1:
        print(i + 1)
    