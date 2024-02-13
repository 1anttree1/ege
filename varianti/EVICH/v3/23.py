def f(n, s):
    if n == s:
        return 1
    if n > s:
        return 0
    return f(n+1,s) + f(n*3,s)
print(f(1,11)*f(11,34))