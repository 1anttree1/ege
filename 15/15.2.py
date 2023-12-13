
for a in range(1, 301):
    h = 0
    for x in range(1, 301):
        for y in range(1, 301):
            if (((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))):
                h += 1
    if h == 300*300:
        print(a)
