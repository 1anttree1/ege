file17 = open('17var09.txt')
s = [int(i) for i in file17]
h = 0
mx = -1000000
for i in range(len(s)-1):
    if s[i] > 0 and s[i+1]>0:
        if (s[i]**0.5)%1 == 0 or (s[i+1]**0.5)%1 ==0:
            h += 1
            mx = max(mx, (s[i] + s[i+1]))
    elif s[i] > 0:
        if (s[i]**0.5)%1 == 0:
            h += 1
            mx = max(mx, (s[i] + s[i+1]))
    elif s[i+1]>0:
        if (s[i+1]**0.5)%1 ==0:
            h += 1
            mx = max(mx, (s[i] + s[i+1]))
    else:
        continue
print(h, mx)