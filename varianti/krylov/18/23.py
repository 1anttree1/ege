def f(n,s):
    if n == s:
        return 1
    if n > s:
        return 0
    return f(n+2, s) + f(n*2, s) + f(n*3, s)
print(f(2, 6) * f(6, 28))