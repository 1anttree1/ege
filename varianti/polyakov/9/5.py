for n in range(100, 1000):
    p = int(str(n)[0]) * int(str(n)[1])
    v = int(str(n)[1]) * int(str(n)[2])
    if p > v :
        r = str(p)+str(v)

    else:
        r = str(v)+str(p)
    if r == '240':
        print(n)