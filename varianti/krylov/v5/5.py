for n in range(1, 100):
    r = bin(n)[2:]
    if n%2 == 0:
        r += '0'
    else: r += '1'
    if r.count('1')%3 == 0:
        r = r[2:]
        r = '11' + r
    else:
        r = r[2:]
        r = '10' + r
    r = int(r, 2)
    if r > 25:
        print(n)
