s = [0]*10000
mx = h = 0
for n in range(1, 1000):
    h += 1
    r = bin(n)[2:] + bin(n%4)[2:]
    s[int(r,2)] = 1
for i in range(0, 10000):
    mx = max(mx, sum(s[i:i+49]))
print(mx)