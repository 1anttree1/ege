def f(n):
    if n <= 1:
        return 0
    if n >1 and n%6 == 0:
        return n +f(n/6- 2)
    if n>1 and n%6 == 0:
        return n +f(n + 6)
print(f(35))
