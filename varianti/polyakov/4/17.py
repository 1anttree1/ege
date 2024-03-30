file = open('17-382.txt')
s = [int(i) for i in file]
mn = 1010101001
mx = h = 0
for i in s:
    if len(str(i)) == 3 and str(i)[-2:] == '11':
        mn = min(mn, i)
print(mn)
for i in range(len(s)-1):
    if ((len(str(s[i])) != 3 and len(str(s[i+1])) == 3) or (len(str(s[i])) == 3 and len(str(s[i+1])) != 3)) and (abs(s[i]-s[i+1]) % mn == 0):
        h += 1
        mx = max(mx, (s[i]+s[i+1]))

print(h,mx)
