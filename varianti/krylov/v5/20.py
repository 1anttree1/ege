def ku(h, s):
    if h == 4 and s>228:
        return 1
    if h != 4 and s>228:
        return 0
    if h == 4 and s<228:
        return 0
    if h %2 != 0:
        return ku(h+1, s+1) or ku(h+1, s*2)
    else:
        return ku(h + 1, s + 1) and ku(h + 1, s * 2)
for i in range(1, 229):
    if ku(1, i):
        print(i)