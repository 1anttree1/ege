import sys
sys.setrecursionlimit(1000000)


def f(n):
    if n >= 10000:
        return 1
    if n<10000 and n%2==0:
        return f(n+3)+7
    if n < 10000 and n % 2 == 1:
        return f(n+1)-3
print(f(50))