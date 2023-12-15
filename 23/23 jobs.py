def f(n,s, k = ''):
    if n == s and k.count('1') >= 1 and k.count('2') >= 1 and k.count('2') >= 1:
        return 1
    if n>s :
        return 0
    return f(n+1, s, k + '1') + f(n + 2, s, k + '2') + f(n*2, s, k + '2')
print(f(3,25))

