def f(n, s):
    if n == s:
        return 1
    if n < s:
        return 0
    return f(n-3,s) + f(n//2, s)
print(f(108, 42) * f(42, 12))