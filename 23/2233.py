def sloji(n):
    sm = 0
    for i in str(n):
        sm += int(i)
    return sm


def umnoj(n):
    pr = 1
    for i in str(n):
        pr = pr * int(i)
    return pr
h = 0

def osn(n,s):
    if n == s:
        return 1
    if n < 10:
        return 0
    return osn(sloji(n), s) + osn(umnoj(n), s)
for i in range(10, 100):
    if osn(i, 8) >= 1:
        h += 1
print(h)