c = 0
for i in open('9-220.csv'):
    f = list(map(int, i.split(';')))
    f.sort()
    if (f[-1]+f[0])%3==0 and (f[-1]-f[-2] == f[1]-f[0]):
        c += 1
print(c)