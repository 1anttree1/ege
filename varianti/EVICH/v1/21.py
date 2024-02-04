def ku(h,s):
    if h == 3 and s > 121:
        return 1
    if h != 3 and s > 121:
        return 0
    if h == 3 and s < 122:
        return 0
    if h % 2 == 0:
        return ku(h+1, s+1) or ku(h+1, s+3) or ku(h+1, s*5)
    else:
        return ku(h + 1, s + 1) and ku(h + 1, s + 3) and ku(h+1, s*5)
for i in range(1, 122):
    if ku(1, i):
        print(i)

def ku1(h,s):
    if (h == 3 or h == 5) and s > 121:
        return 1
    if h != 5 and s > 121:
        return 0
    if h == 5 and s < 122:
        return 0
    if h % 2 == 0:
        return ku1(h+1, s+1) or ku1(h+1, s+3) or ku1(h+1, s*5)
    else:
        return ku1(h + 1, s + 1) and ku1(h + 1, s + 3) and ku1(h+1, s*5)
for i in range(1, 122):
    if ku1(1, i):
        print(i,'----------------')
