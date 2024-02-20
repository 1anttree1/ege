for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '00'
    else:
        r += '11'
    if int(r,2) < 102:
        print(n)