h = 0
for i in open('9-223.csv'):
    f = list(map(int, i.split(';')))
    l = [int(x) for x in f if f.count(x) == 3]
    j = [int(x) for x in f if f.count(x) == 1]
    if len(l) == 3 and len(j) == 4:
        if sum(j)/len(j) <= l[0]:
            h += 1
print(h)
