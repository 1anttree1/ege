from sys import *
setrecursionlimit(10000)

def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return s[n+1] - s[n+2] + 7
s = [0]*3000

for i in range(2900, 0, -1):
    s[i] = f(i)

print(s[15]-s[24])