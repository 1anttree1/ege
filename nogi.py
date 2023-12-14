def sloji(n, k = ''):
    n = str(n)
    k = int(k)
    for i in n:
        k += int(i)
    return sloji(n)
print(sloji(11))



        