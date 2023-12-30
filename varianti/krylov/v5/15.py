for a in range(1, 301):
    h = 0
    for x in range(1, 301):
        if ((x%13 == 0) <= (x%21 != 0) or (x+a>= 500)):
            h += 1
    if h == 300:
        print(a)
        break