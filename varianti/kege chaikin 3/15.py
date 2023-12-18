for a in range(1, 301):
    h = 0
    for x in range(1, 301):
        if (((x%12 == 0) and (x&4 == 0)) <= (x+1 > a)):
            h += 1
    if h == 300:
        print(a)

