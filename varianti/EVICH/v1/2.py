print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(x == z) and (not (w <= (y and z)))):
                    print(x, y, w, z)