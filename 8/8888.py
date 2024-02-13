from itertools import *
a = permutations('0123456789abcdef', r = 4)
s = []
for i in a:
    s.append(list(i))
for i in s:
    for j in range(len(i)):
        i[j] = i[j].replace('a', '10')
        i[j] = i[j].replace('b', '11')
        i[j] = i[j].replace('c', '12')
        i[j] = i[j].replace('d', '13')
        i[j] = i[j].replace('e', '14')
        i[j] = i[j].replace('f', '15')
h = 0
for i in s:
    ch = nch = 0
    lch = []
    lnch = []
    for j in range(len(i)):
        if i[0] != '0':
            if int(i[j])%2 == 0:
                lch.append(i[j])
                ch += 1
            else:
                nch += 1
                lnch.append(i[j])
        else:
            break
    if ch == 2 and nch == 2:
        if int(lch[0]) + int(lch[1]) == int(lnch[0]) + int(lnch[1]):
            h += 1
print(h)