from math import *
for i in range(174457, 174506):
    h = 0
    if sqrt(i) %1 == 0:
        h += 1
    for g in range(2, round(sqrt(i))):
        if i%g==0:
            h += 2
        if h >2 :
            break
    if h == 2:
        for g in range(2, round(sqrt(i))):
            if i % g == 0:
                print(g,i//g)
                break