def ku(h, k):
    if h == 3 and k > 81:
        return 1
    if h == 3 and k < 82:
        return 0
    if h != 3 and k > 82:
        return 0
    if h % 2 == 0:
        return ku(h+1, k+2) or ku(h+1, k+4) or ku(h+1, k*3)
    else:
        return ku(h + 1, k + 2) and ku(h+1, k + 4) and ku(h+1, k * 3)
for i in range(1, 82):
    if ku(1, i):
        print(i)
print('--------------------')
def ku1(h, k):
    if (h == 3 or h == 5) and k > 81:
        return 1
    if h == 5 and k < 82:
        return 0
    if h != 5 and k > 82:
        return 0
    if h % 2 == 0:
        return ku1(h+1, k+2) or ku1(h+1, k+4) or ku1(h+1, k*3)
    else:
        return ku1(h + 1, k + 2) and ku1(h+1, k + 4) and ku1(h+1, k * 3)
for i in range(1, 82):
    if ku1(1, i):
        print(i)