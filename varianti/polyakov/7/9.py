c = 0
for i in open('9-160.csv'):
    f = list(map(int, i.split(';')))
    f.sort()
    if (f[-1] < sum(f[:-1])) and ((f[-1] + f[0]) == (f[2]+ f[1])):
        c += 1
print(c)