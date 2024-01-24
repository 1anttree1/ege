def f(n, s):
    if n == s:
        return 1
    if n>s or n == 16:
        return 0
    return f(n+1,s) + f(n+3, s) + f(n**2, s)
print(f(3,20)*f(20,26))

