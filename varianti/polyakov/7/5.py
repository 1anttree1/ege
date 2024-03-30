for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1') > r.count('0'):
        r += '0'
    else:
        r += '11'
    if int(r, 2) > 2019:
        print(n)