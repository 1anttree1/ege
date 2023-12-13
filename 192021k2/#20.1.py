def ku(h, k1,k2):
    if h == 4 and (k1+k2)>=77:
        return 1
    if h != 4 and (k1+k2)>=77:
        return 0
    if h == 4 and (k1+k2)<77:
        return 0
    if h%2 ==1:
        return ku(h+1, k1+1,k2) or ku(h+1, k1*2,k2) or ku(h+1, k1,k2+1) or ku(h+1, k1,k2*2)
    else:
        return ku(h+1, k1+1,k2) and ku(h+1, k1*2,k2) and ku(h+1, k1,k2+1) and ku(h+1, k1,k2*2)
for i in range(1, 70):
    if ku(1,7,i):
        print(i)