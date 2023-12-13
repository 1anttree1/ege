def f(n):
    if n>1:
        return f(n-1) + n
    if n==1:
        return 0
def g(n):
    if n >1:
        return g(n -1) *n
    if n == 1:
        return 1
print(g(5)+f(5))
