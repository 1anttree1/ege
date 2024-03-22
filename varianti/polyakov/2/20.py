def ku(h,x,y):
    if h == 4 and x**2+y**2 > 196:
        return 1
    if h == 4 and x**2+y**2 <= 196:
        return 0
    if h != 4 and x ** 2 + y ** 2 > 196:
        return 0
    if h %2 != 0:
        return ku(h+1, x*2, y) or ku(h+1, x, y+3) or ku(h+1, x, y+4)
    else:
        return ku(h + 1, x * 2, y) and ku(h + 1, x, y + 3) and ku(h + 1, x, y + 4)
for i in range(1, 14):
    if ku(1, 3, i):
        print(i)