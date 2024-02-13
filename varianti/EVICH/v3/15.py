for a in range(301, 601):
    h = True
    for x in range(1, 601):
        if ((((x%a != 0) <= ((x%27 == 0)<= (x % 89 != 0))) and (a > 300))) == False:
            h = False
            break
    else:
        print(a)

    # if h == 600:
    #     print(a)
    #     break