def f(n):
    if n == 0 or n == 1:
        return 1
    if n > 1 and n%2 == 0:
        return 10+f(n//2)
    if n>1 and n%2 != 0:
        return 2 * f(n-3)
print(f(60))