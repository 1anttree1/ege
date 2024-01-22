for n in range(0, 100):
    sm = 0
    s = '>' + '1'* 16 + '2'*n + '3' * 16
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s :
            s = s.replace('>1', '1>')
        if '>2' in s :
            s = s.replace('>2', '>3')
        if '>3' in s :
            s = s.replace('>3', '>1')
    for i in s[:-1]:
        sm += int(i)
    for i in range(2, int(sm**0.5)+1):
        if sm%i == 0:
            break
    else: print(n)

        