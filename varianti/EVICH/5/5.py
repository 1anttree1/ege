h = 0
for n in range(1, 1000):
    r = bin(n)[2:]
    if n%2== 0:
        r += '00'
    else: r+= '10'
    if r.count('1')%2 == 0:
        r += '0'
    else: r += '1'
    if 130<=int(r, 2)<=350:
        h += 1
print(h)