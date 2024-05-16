c = 0
for i in open('9-159.csv'):
    f = list(map(int, i.split(';')))
    ch = [int(x) for x in f if x%2 == 0]
    nch = [int(x) for x in f if x % 2 != 0]
    if (sum(ch)<sum(nch)):
        c += 1

print(c)
