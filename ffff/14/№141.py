n = 49**10 + 7**30 - 49
h = 0
while n> 0:
    if n %7 == 6:
        h += 1
    n //= 7
print(h)