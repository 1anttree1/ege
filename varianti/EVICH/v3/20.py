def ku(h, k):
    if h == 4 and k > 135 :
        return 1
    if h != 4 and k > 135:
        return 0
    if h == 4 and k < 135:
        return 0
    if h % 2 != 0:
        return ku(h + 1, k + 1) or ku(h + 1, k*4-3)
    else:
        return ku(h + 1, k + 1) and ku(h + 1, k * 4 - 3)
for i in range(1, 136):
    if ku(1, i):
        print(i)