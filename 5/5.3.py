for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1') > r.count('0') :
        r += '1'
    elif r.count('1') == r.count('0'):
        r += '0'
    r = int(r, 2)
    if r>80:
        print(r)