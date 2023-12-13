def ku(h,k):
    if h == 3 and k>58:
        return 1
    if h != 3 and k>58:
        return 0
    if h == 3 and k<59:
        return 0
    if h%2 == 0:
        return ku(h+1, k+1) or ku(h+1, k+3) or ku(h+1, k*4)
    else:
        return ku(h + 1, k + 1) and ku(h + 1, k + 3) and ku(h + 1, k * 4)
for i in range(1, 59):
    if ku(1, i):
        print(i)
#ОТВЕТ4
