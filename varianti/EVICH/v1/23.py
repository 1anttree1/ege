def f(n, s):
    if n == s:
        return 1
    if n > s or n == 11:
        return 0
    if n < s:
        return f(n+1, s) + f(n*2,s) + f(n*3, s)
print(f(5,19)*f(19,39))

        