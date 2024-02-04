for a in range(1, 301):
    h = 0
    for x in range(1,301):
        if ((x&56 != 0) <= ((x&a == 0)<= (x&35 != 0))):
            h += 1
    if h == 300:
        print(a)