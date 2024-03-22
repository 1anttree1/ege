h = 0
for n in range(100000000, 1000000000, 10):
    r = bin(sum(map(int, list(str(n)))))[2:]
    if r.count('1')%2 == 0:
        r = '1' + r + '00'
    else: r = '10' + r + '1'
    if int(r, 2) == 21:
        h += 1
        print(r, n)
print(h)
