for n in range(1, 1000):
    r = bin(n)[2:]
    f = r.rfind('0')
    if f != -1:
        r = r[:f] + r[:2] + r[f+1:]
        r = r[::-1]
    else:
        continue
    if int(r, 2) == 123:
        print(n)