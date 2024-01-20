def ku(h, k1,k2):
    if h == 3 and k1+k2 >= 142:
        return 1
    if h != 3 and k1+k2 >= 142:
        return 0
    if h == 3 and k1+k2 < 142:
        return 0
    if h%2 == 0:
        return (ku(h+1, k1+2, k2) or ku(h+1, k1*2, k2)) or (ku(h+1, k1, k2+2) or ku(h+1,k1, k2*2))
    else:
        return (ku(h + 1, k1 + 2, k2) or ku(h + 1, k1 * 2, k2)) or (ku(h + 1, k1, k2 + 2) or ku(h + 1, k1, k2 * 2))
for i in range(1,139):
    if ku(1,2, i):
        print(i)