a = 10000000


for n in range(1, 1000):
    r = ''
    help = n
    while help > 0:
        r += str(help %3)
        help //= 3
    r = r[::-1]
    r += str(n %3)
    r = int(r, 3)
    if r > 999:
        a = min(a, r)
print(a)