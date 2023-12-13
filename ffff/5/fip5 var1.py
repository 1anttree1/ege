def perevod(n, s):
    string = ""
    while n != 0:
        string += str(n % s)
        n //= s
    return string[::-1]
mn = -10000000000000000000000
for i in range(5, 1000):
    n = perevod(i, 4)
    if i%4 == 0:
        n += n[-2:]
    else:
        ost = (i%4)*2
        n += perevod(ost,4)
    n = int(n, 4)
    if n<261:
        mn = max(mn, i)
print(mn)