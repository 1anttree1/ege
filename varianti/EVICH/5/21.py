def ku(h, k):
    if h ==3 and k>= 78:
        return 1
    if h != 3 and k>= 78:
        return 0
    if h == 3 and k < 78:
        return 0
    if h % 2 == 0:
        return ku(h+1, k+1) or ku(h +1, k +3) or ku(h+1, k *4 )
    else: return ku(h+1, k+1) and ku(h +1, k +3) and ku(h+1, k *4 )
for i in range(1, 78):
    if ku(1, i):
        print(i)

def ku1(h, k):
    if (h ==3 or h == 5 )and k>= 78:
        return 1
    if h != 5 and k>= 78:
        return 0
    if h == 5 and k < 78:
        return 0
    if h % 2 == 0:
        return ku1(h+1, k+1) or ku1(h +1, k +3) or ku1(h+1, k *4 )
    else: return ku1(h+1, k+1) and ku1(h +1, k +3) and ku1(h+1, k *4 )
for i in range(1, 78):
    if ku1(1, i):
        print(i, '-----------------')