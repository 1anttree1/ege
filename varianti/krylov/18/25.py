h = 0
for i in range(550001, 1000000):
    d = 0
    for j in range(i//2, 2, -1):
        if i % j == 0:
            d = j
            break
    for j in range(2, int(d**0.5)+1):
        if d%j == 0:
            print(i, d)
            h += 1
            break
    if h == 6:
        break