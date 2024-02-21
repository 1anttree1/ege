def f(n,s):
    if n == s:
        return 1
    if n < s:
        return 0
    return f(n/2, s) + f(n-1, s)
print(f(30,7))