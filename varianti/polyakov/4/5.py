def perevod(n, s):
    string = ""
    while n != 0:
        string += str(n % s)
        n //= s
    return string[::-1]
for n in range(1, 1000):
    r = perevod(n, 3)
    if n%3 == 0:
        r = '1' + r + '02'
    else:
        r += perevod((n%3)*4, 3)
    if int(r, 3) < 199:
        print(n)


