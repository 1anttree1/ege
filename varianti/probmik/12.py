s = '3' * 85
while '133' in s or '333' in s:
    if '133' in s:
        s = s.replace('133','1', 1)
    else:
        s=s.replace('333', '13', 1)
print(s)