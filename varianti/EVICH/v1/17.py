file = open('17.txt')
s = [int(i) for i in file]
mx = mx1 = 0
h =0
for i in s:
    if len(str(i)) == 3 and str(i)[-1] == '4':
        mx = max(mx,i)
print(mx)
for i in range(len(s)-1):
    if ((str(s[i])[-1] == '3' and str(s[i+1])[-1] != "3") and ((s[i+1] + s[i]) % mx)!= 0) or ((str(s[i+1])[-1] == '3' and str(s[i])[-1] != "3") and ((s[i+1] + s[i]) % mx)!= 0):
        h += 1
        mx1 = max(mx1, s[i]+s[i+1])

print(h, mx1)