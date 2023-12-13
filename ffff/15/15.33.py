for a in range(1, 301):
    h = 0
    for x in range(1 , 301):
        if ((a < 50) and ((x%a != 0) <= ((x%10 == 0) <= (x%12 != 0)))):
            h += 1
    if h == 300:
        print(a)
