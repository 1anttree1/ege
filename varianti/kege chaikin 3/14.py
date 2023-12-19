for x in range(1,32):
    a = 7*32**2+2*32+x
    b = 1*32**3+12*32**2+x*32+7
    c = a + b + x**5
    if c%x == 0:
        print(c/x, x)