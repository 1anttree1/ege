a = 4**2020 + 2**2017 - 15
h = 0
while a>0:
    if a%2 == 1:
        h += 1
    a = a//2
print(h)
