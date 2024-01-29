for n in range(100):
    d = 0
    s = '>' + '0'*31 + '1' * n + '2'*47
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '21>', 1)
        if '>2' in s:
            s = s.replace('>2', '12>', 1)
        if '>0' in s:
            s = s.replace('>0', '2>', 1)
    sm = s.count('1') + s.count('2')*2
    for i in range(2, int(sm**0.5)):
        if sm%i == 0:
            break
    else:
        print(n)