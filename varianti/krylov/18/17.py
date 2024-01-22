file17 = open('17var18.txt')
s = [int(i) for i in file17]
mn = 890234500
h = 0
for i in range(len(s)-1):
    if (s[i] > 0 and s[i+1] >0) and ((s[i] + s[i+1]) > 49):
        h += 1
        mn = min(mn, s[i] * s[i+1])
print(h, mn)
        