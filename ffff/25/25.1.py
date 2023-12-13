from math import *
for i in range(245690,245757):
    h = 0
    if sqrt(i)%1==0:
        h +=1
    for j in range(2, round(sqrt(i))):
        if i%j == 0:
            h += 2
        if h > 2:
            break
    if h == 0:
        print(i-245689, i)

