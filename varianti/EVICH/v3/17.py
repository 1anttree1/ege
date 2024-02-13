file = open('17.txt')
s = [int(i) for i in file]
mn = 293847502394785
h = sm = 0
mx = 0
count = 0
for i in s:
    mn = min(mn,i)
    if i % 4 == 0:
        h += 1
        sm += i
sm = sm/h
for i in range(len(s)-1):
    if (s[i] % mn == 0 or s[i + 1] % mn == 0) and (s[i] + s[i+1] < sm):
        count += 1
        mx = max(mx, s[i] + s[i+1])
print(mx, count)
        