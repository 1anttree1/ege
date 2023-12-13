file17 = open("17.txt")
a = []
mx = -1000000000
h=0
for i in file17:
    a.append(int(i))
for i in range(len(a)-1):
    if a[i]%3 == 0 or a[i+1]%3 == 0:
        mx = max(mx, (a[i] + a[i+1]))
        h += 1
print(h, mx)