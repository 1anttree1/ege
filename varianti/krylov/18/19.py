def ku(k1, k2, h):
    if h == 3 and k1+k2 >= 123:
        return 1
    if h != 3 and k1+k2 >= 123:
        return 0
    if h == 3 and k1 + k2 < 123:
        return 0
    if h%2 == 0:
        return ku(k1+1, k2, h+1) or ku(k1*2, k2, h+1) or ku(k1, k2+1, h+1) or ku(k1, k2*2, h+1)
    else:
        return ku(k1 + 1, k2, h + 1) or ku(k1 * 2, k2, h + 1) or ku(k1, k2 + 1, h + 1) or ku(k1, k2 * 2, h + 1)
for i in range(1, 114):
    if ku(9, i, 1):
        print(i)


