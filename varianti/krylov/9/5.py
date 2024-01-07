for n in range(100, 1000):
    n = str(n)
    r1 = str(int(n[0])**2 + int(n[1])**2)
    r2 = str(int(n[1])**2 + int(n[2])**2)
    r = r1+r2
    if r == '9752':
         print(n)
    