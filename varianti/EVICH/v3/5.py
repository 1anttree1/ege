for n in range(1, 1000):
    r = bin(n)[2:]
    if int(r)%2 == 0:
        r += '01'
    else:
        r = '1'+ r + '10'
    if int(r,2) > 214:
        print(n)