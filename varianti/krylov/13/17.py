a = open('17var13.txt')
f = [int(i) for i in a]
h = mx =0
for i in range(len(f)-1):
    if str(f[i])[-1] == '5' and str(f[i+1])[-1] == '5':
        h += 1
        mx = max(mx, abs(f[i]-f[i+1]))
print(h,mx)
    