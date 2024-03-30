def f(n, s):
    if n == s:
        return 1
    if n > s or n == 23:
        return 0
    if n<s :
        return f(n + 2, s) + f(n * 3, s) + f(n*5, s)
print(f(1, 13)*f(13,75))
