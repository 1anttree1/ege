for a in range(1, 301):
    h = 0
    for x in range(1, 301):
        for y in range(1, 301):
            if ((x < a) <= (x**2 < 100)) and ((y**2 <= 64) <= (y <= a)):
                h += 1
            else: break
    if h == 300 * 300:
        print(a)
