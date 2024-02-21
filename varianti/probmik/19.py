def ku(h,k1,k2):
    if h == 2 and k1+k2 >= 87:
        return 1
    if h != 2 and k1+k2 >= 87:
        return 0
    if h == 2 and k1+k2 < 87:
        return 0
    if h%2 != 0:
        return ku(h+1, k1+1, k2) or ku(h+1, k1*3, k2) or ku(h+1, k1, k2+1) or ku(h+1, k1, k2*3)
    else:
        return ku(h + 1, k1 + 1, k2) and ku(h + 1, k1 * 3, k2) and ku(h + 1, k1, k2 + 1) and ku(h + 1, k1, k2 * 3)
for i in range(1, 80):
    if ku(1, 7, i):
        print(i)
