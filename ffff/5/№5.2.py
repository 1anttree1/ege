for n in range(100, 1000):
    a = str(n)
    sum1 = str(int(a[0]) + int(a[1]))
    sum2 = str(int(a[1]) + int(a[2]))
    if int(sum1) > int(sum2):
        sum3 = sum1 + sum2
    else:
        sum3 = sum2 + sum1
    if int(sum3) == 1412:
        print(a)
