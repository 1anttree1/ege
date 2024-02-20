for i in range(153222, 153271):
    h = 0
    for j in range(1, 391):
        if ((i-(j**2))**0.5)%1 == 0:
            h += 1
            print(j, (i-(j**2))**0.5, i)

