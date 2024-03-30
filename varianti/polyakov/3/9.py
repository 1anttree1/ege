count = 0
for i in open('9-225.csv'):
    f = list(map(int, i.split(';')))
    l = [int(x) for x in f if f.count(x) == 2]
    f.sort()
    if ((f[0] + f[-1])**2 < (f[1]**2+f[2]**2+f[3]**2)) and ( len(l) == 2):
        count += 1
print(count)