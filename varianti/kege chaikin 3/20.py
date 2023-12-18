def ku(h, k):
    if h == 4 and k > 71:
        return 1
    if h != 4 and k > 71:
        return 0
    if h == 4 and k < 71:
        return 0
    if h % 2 == 1:
        return ku(h+1, k+3) or ku(h+1, k+5) or ku(h+1, k*2)
    else:
        return ku(h+1, k+3) and ku(h+1, k+5) and ku(h+1, k*2)
for i in range(1, 72):
    if ku(1, i):
        print(i)