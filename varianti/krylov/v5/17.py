file17 = open('17var05.txt')
s = [int(i) for i in file17]
mx = 0
h = 0
for i in range(len(s)-1):
    if s[i]+s[i+1] == 99991:
        h += 1
        mx = max(mx, s[i]**2+s[i+1]**2)
print(h, mx)