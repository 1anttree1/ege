for n in range(1, 1000):
    r = bin(n - (n%8) + (n%2))[2:]
    r += str(r.count('1')%2)
    r += str(r.count('1') % 2)
    if int(r, 2) > 97:
        print(int(r, 2))
        break
