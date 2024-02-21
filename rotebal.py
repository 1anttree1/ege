def perevod(n, s):
    string = ""
    while n != 0:
        string += str(n % s)
        n //= s
    return string[::-1]

for n in range(10, 1000):
    r = perevod(n, 5)
    if n%5 == 0:
        r += r[-3:]
    else:
        r = perevod((n%5)*5, 5) + r
    if int(r,5) > 375:
        print(n)
        break