mx = 0
for i in range(4, 1000):
    s = '1' + '2'*i
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    mx = max(mx, s.count('2'))
print(mx)