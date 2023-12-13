def perevod(n, s):
    string = ""
    while n != 0:
        string += str(n % s)
        n //= s
    return string[::-1]


a = []
for i in range(1, 1000):
    n = perevod(i, 3)
    if len(n) % 2 != 0:
        n = '1' + n
    sim = 0
    for s in n:
        sim = sim + int(s)
    if sim % 2 == 0:
        n = n + n[:2]
    else:
        ost = int(n) % 5
        n += perevod(ost, 3)
    if n[0] == '2':
        n = n[1:]
        while n[0] == '0':
            n = n[1:]
    l = len(n)
    if n[l - 1] == n[l - 2]:
        n = n[:-1]
    if int(n, 3) > 150:
        a.append(int(n, 3))
print(min(a))