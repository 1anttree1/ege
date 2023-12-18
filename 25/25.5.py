import math
for i in range(460000001, 4600000000):
    dl = 0
    mx = 0
    if math.sqrt(i)%1==0:
        dl += 1
    for j in range(2, round(math.sqrt(i))):
        if i%j == 0:
            dl += 2
        if dl > 5:
            break
    if dl > 5:ц
        for j in range(i//2 + 1, 1, -1):
            if i%j == 0:
                mx += 1
                if mx == 5:
                    print(j, i)
                    break