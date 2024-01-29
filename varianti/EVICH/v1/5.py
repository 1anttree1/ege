for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1')% 2 == 0:
        r += '10'
        r = '110' + r[3:]
    else:
        r += '101'
        r = '10' + r[2:]
    if int(r, 2) > 120:
        print(n)
        break