file17 = open('17_12249.txt')
f = [int(i) for i in file17]
h = 0
mx = 99683
mxsum = 0
for i in range(len(f)-2):
    sm = 0
    if (str(f[i])[-1] == '3' or str(f[i+1])[-1] == '3' or str(f[i+2])[-1] == '3') and ((f[i] + f[i+1] + f[i+2]) < mx):
        sm = f[i] + f[i+1] + f[i+2]
        mxsum = max(mxsum, sm)
        h += 1
print(h, mxsum)