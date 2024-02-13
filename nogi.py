def p(n, s):
    string = ""
    if n == 0:
        string += '0'
    while n > 0:
        string += str(n % s)
        n //= s

    return string[::-1]
mn = 10101010

for n in range(1,1000):
    r = p(n, 3)
    if len(r)%2 != 0:
        r = '1' + r
    sm = r.count('1') + r.count('2')*2
    if sm%2 == 0:
        r += r[:2]
    else:
        ost = p(n%5, 3)
        r += ost
    if r[0] == '2':
        r = r[1:]
        while r[0] == '0':
            r = r[1:]
    if len(r)>1:
        if r[-1] == r[-2]:
            r = r[:-1]
    r = int(r,3)
    if r > 150:
        mn = min(mn, r)
print(mn)