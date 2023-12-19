import sys
sys.setrecursionlimit(10000)
def f(x):
    if x <= 2:
        return 2**x
    if x > 2 and x%2 == 0:
        return f(x//2)
    if x > 2 and x%2 == 1:
        return f(x+1) + f(x-4)
s = [1]*5000
for i in range(1, 5000):
    s[i] = f(i)
print(s[4202])