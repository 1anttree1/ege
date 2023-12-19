s = '1' * 128
h = 0
while '333' in s or '11' in s:
    if '333' in s:
        s = s.replace('333', '1', 1)
    else:
        s = s.replace('11', '3', 1)
        h += 2

print(128 - s.count('1'), h)