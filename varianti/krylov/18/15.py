for a in range(1, 301):
    h = 0
    for x in range(1, 301):
        for y in range(1, 301):
            if ((x >= a) or (y >= a) or (x*y <= 270)):
                h += 1
    if h == 300*300:
        print(a)