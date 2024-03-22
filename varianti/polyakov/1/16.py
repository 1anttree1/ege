import sys
sys.setrecursionlimit(10000)
h = 0
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n-1)
for n in range(1, 101):
    if (f(2023)//f(n) ) % 2 ==0:
        h += 1
print(h)