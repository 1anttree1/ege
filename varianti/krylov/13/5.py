for n in range(1, 1000):
    f = 0
    r = bin(n-(n%4))[2:]
    r += str(r.count('1')%2)
    r += str(r.count('1') % 2)
    if int(r,2) > 56:
        print(int(r,2))
        break
    

