file = open('17-384.txt')
s = [int(i) for i in file]
mx = h = 0
for i in range(len(s)-1):
    if (len(str(s[i])) == 2 and len(str(s[i+1])) != 2) or (len(str(s[i])) != 2 and len(str(s[i+1])) == 2):
        mx = max(s[i]+s[i+1], mx)
for i in range(len(s)):
    if s[i] > mx:
        h += 1
print(h)