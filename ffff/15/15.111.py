for a in range(1, 301):
    h = 0
    for x in range(1, 301):
        if ((72%x ==0)<= (90%x != 0) or (a-x>80)):
            h += 1
    if h == 300:
        print(a)
