file = open('17-383.txt')
mx = 0
mx1 = 0
h = 0

f = [int(i) for i in file]
for i in f:
    if len(str(i)) == 2:
        mx = max(mx, i)
print(mx)
for i in range(len(f)-1):
    if (len(str(abs(f[i]))) == 2 or len(str(abs(f[i+1]))) == 2) and ((f[i] + f[i+1]) < mx):
        h += 1
        mx1 = max(mx1, f[i] + f[i+1])
print(h, mx1)