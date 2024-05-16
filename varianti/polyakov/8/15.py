for a in range(1, 301):
    h = 0
    for x in range(1, 301):
        if ((a + x < 123) <= ((x%5 == 0) <= (x % 7 != 0))):
            h += 1
    if h == 300:
        print(a)