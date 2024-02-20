for x in range(10000):
    h = 0
    f = 243**5 + 3**7 - 2 - x
    while f != 0:
        if f%3 == 2:
            h += 1
        f //= 3
    if h == 20:
        print(x)
