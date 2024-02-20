file = open('17.txt')
s = [int(i) for i in file]
mx = h = 0
for i in range(len(s)-1):
    if s[i]%5 == 0 and s[i+1] % 5 == 0:
        h += 1
        mx = max(mx, s[i] + s[i+1])
print(h, mx)
