file = open('17.txt')
s = [int(i) for i in file]
h = 0
mn = 290093847520398457
for i in range(1, len(s)-1):
    if s[i-1]<s[i]>s[i+1]:
        h += 1
        mn = min(mn, s[i])
print(h,mn)
