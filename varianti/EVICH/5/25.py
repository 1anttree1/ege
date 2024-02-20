h = 0
mn = 457823907289034597804235
for i in range(50000000, 60000001):
    s = []
    if i%911 == 0:
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                s.append(i)
    if len(s) == 3:
        h += 1
        mn = min(mn, i)
print(h, mn)