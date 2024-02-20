file = open('17.txt')
s = [int(i) for i in file]
h = 0
mn = 72358490
for i in s:
    if '6' in str(i):
        h += 1
        mn = min(mn, i)
print(h, mn)