file17 = open('17var01.txt')
a = []
h = 0
mx = 0
sm = 0
mn = 1000000000
for i in file17:
    a.append(int(i))
    if int(i) % 100 == 25:
        mn = min(mn, int(i))
for i in range(len(a) -2):
    if ((len(str(a[i])) == 2) and (len(str(a[i+1]))!= 2) and (len(str(a[i+2])) != 2))\
        or ((len(str(a[i])) != 2) and (len(str(a[i+1])) == 2) and (len(str(a[i+2])) != 2))\
        or ((len(str(a[i])) != 2) and (len(str(a[i+1]))!= 2) and (len(str(a[i+2])) == 2)):
        if (a[i] + a[i+1] + a[i+2]) < mn:
            h += 1
            sm = a[i] + a[i+1] + a[i+2]
            mx = max(mx, sm)
print(h, mx)



