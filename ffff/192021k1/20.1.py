def ku(h,k):
    if h==4 and k>67:
        return 1
    if h != 4 and k>67:
        return 0
    if h == 4 and k<67:
        return 0
    if h%2==1:
        return ku(h+1,k+1) or ku(h+1,k+4) or ku(h+1,k*5)
    else:
        return ku(h+1,k+1) and ku(h+1,k+4) and ku(h+1,k*5)
for i in range(1, 68):
    if ku(1, i):
        print(i)

