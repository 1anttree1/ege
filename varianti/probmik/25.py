for i in range(51120,89080+1):
    dl = 0
    s = []
    f = []
    for j in range(2, i):
        if i%j == 0:
            s.append(j)
        else:
            continue


    for j in s:
        if j%30 == 0:
            dl += 1
            f.append(j)
    if dl == 2:
        print(i,f)
