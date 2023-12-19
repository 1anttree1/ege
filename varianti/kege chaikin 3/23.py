def f(n, s, k=''):
    if n == s and k[-3:] == 'BAB':
        return 1
    if n > s:
        return 0
    return f(n+1, s, k + 'A') + f(n*2, s, k + 'B') +f(n+5, s, k + 'C')
print(f(5, 62))
