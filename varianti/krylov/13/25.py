h = 0
for x in range(850001, 900000):
    dmx = dmn = 0
    f = 0
    for i in range(2, x//2):
        if x%i == 0:
            dmn = i
            dmx = x//i
            break
    f = (dmx - dmn)
    if f > 0 and f%7 == 0:
        h += 1
        print(x, f)
    if h == 6:
        break