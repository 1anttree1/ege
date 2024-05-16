for a in range(1,10001):
    h = 0
    for x in range(1, 10001):
        if ((((x%10==0) and (x%26==0)) and (x >= 300)) <= (a<=x)):
            h += 1
    if h == 10000:
        print(a)