for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1') % 2 != 0:
        r += '11'
    else:
        r = '11' + r
    if int(r, 2) > 102:
        print(n)