def fun(n):
    if n > 1:
        return fun(n-1) *n
    if n == 1:
        return 1
print(fun(5))
