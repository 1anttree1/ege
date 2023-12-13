file17 = open("17_1.txt")
a = []
mx = -1
h = 0
for i in file17:
    a.append(int(i))
for i in range(len(a)-1):
    for x in range((i+1), len(a)):
        if ((a[i] % 160) != (a[x] % 160)) and (a[i] % 7 ==0 or a[x] % 7 == 0):
            h += 1
            mx = max(mx, (a[i]+a[x]))
print(mx, h)