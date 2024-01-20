for a in range(1, 301):
    h = 0
    for x in range(1, 301):
        if (((x % a) != 0) <= (((x%18) == 0) <= ((x%81) != 0))):
            h += 1
    if h == 300:
        print(a)