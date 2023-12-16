import math
h = 0
for i in range(185311, 185331):
    dl = 2
    if math.sqrt(i)%1 == 0:
        dl += 1
        continue
    for j in range(2, round(math.sqrt(i))):
        if i%j == 0:
            dl += 2
        if dl > 4:
            break
    if dl == 4:
        for j in range(1, round(math.sqrt(i))):
            if i%j == 0:
                print(j, i//j, i)
