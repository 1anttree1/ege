file17 = open('17.12.txt')
a = []
mx = -1
h = 0
for i in file17:
    a.append(int(i))
for i in range(len(a)-1):
    for j in range(i + 1, len(a)):
        if ((a[i]-a[j])%2==0) and (a[i]%31 == 0 or a[j]%31 == 0):
            mx = max(mx, a[i] + a[j])
            h += 1
print(h, mx)