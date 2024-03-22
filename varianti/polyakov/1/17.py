file = open('17-385.txt')
mn = 140235789
s = [int(i) for i in file]
h = 0
q = 2011
mx = 0
for i in range(len(s)-1):
    if s[i]>q and s[i+1]>q:
        h += 1
        mx = max(mx, sum(map(int, list(str(s[i+1]))))+sum(map(int, list(str(s[i])))))
print(h, mx)


