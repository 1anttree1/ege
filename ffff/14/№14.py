n = 4**2020 + 2**2017 - 15
h = 0
while n > 0:
    if n%2 == 1:
        h += 1
    n = n//2
print(h)