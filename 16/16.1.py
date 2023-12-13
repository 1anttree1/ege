def f(n):
    if n>1:
        return f(n-1)*f(n-1)-f(n-1)*n +2 *n
    if n == 1:
        return 1
print(f(5))