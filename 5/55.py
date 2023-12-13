a = 1000000000
m = []
for n in range(10, 1001):
    l = bin(n)[3:]
    while l[0] == "0" and len(l)>1:
        l = l[1:]
    l = int(l, 2)
    r = n - l
    if (r in m) == False:
        m.append(r)
print(m)