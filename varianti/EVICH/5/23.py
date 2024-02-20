def f(n, s):
    if n == s:
        return 1
    if n > s:
        return 0
    if n < s:
        return f(n+1, s) + f(n*2, s) + f(n*5, s)
print(f(1, 10)* f(10, 20)* f(20, 38))