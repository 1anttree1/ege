print('z y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x == y) or not(y <= w) or z) == 0:
                    print(x ,y, w,z)