file17 = open('17_10100.txt')
a =[]
mx = mx1 =-1000
h = 0
for i in file17:
    a.append(int(i))
for i in a:
    if str(i)[-2:] == "13":
        mx = max(mx, i)
print(mx)
print(len(a))
for i in range(len(a)-2):
    g = 0
    if (len(str(a[i])) == 3):
        g += 1
    if (len(str(a[i+1])) == 3):
        g += 1
    if (len(str(a[i + 2])) == 3):
        g += 1
    if g == 2 and (a[i] + a[i+1] + a[i+2]) < mx:
        mx1 = max(mx1, a[i] + a[i+1] + a[i+2])
        h += 1



print(h)
print(mx1)

