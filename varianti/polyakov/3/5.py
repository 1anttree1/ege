for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r + '00'
    else: r = '11' + r
    if int(r, 2) > 411:
        print(n)
        break