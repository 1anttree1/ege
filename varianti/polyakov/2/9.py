count = 0
for i in open('9-226.csv'):
    f = list(map(int, i.split(';')))
    l = [int(x) for x in f if f.count(x) == 2]
    c = [int(x) for x in f if f.count(x) == 1]
    if len(c) == 3 and len(l) == 4:
        if max(f) in c:
            print(sum(f))
