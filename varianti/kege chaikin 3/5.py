def p(n, s):
    f = ''
    while n>0:
        f += str(n%7)
        n //= s
    return f[::-1]
for n in range(1, 1000):
    r = p(n, 7)
    sm = 0
    for i in r:
         sm += int(i)
    if sm % 2 == 0: r+='0'
    else:
        r = list(r)
        r[0] = '6'
        r = ''.join(r)
    r = int(r, 7)
    if r<119:
        print(r)


