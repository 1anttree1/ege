import sys
sys.setrecursionlimit(10000)
def f(n):
    if n < 3:
        return 3
    if n >= 3:
        return 2*n + 5 + s[n-2]
# print(f(3027)-f(3023))
s = [0] * 5555
for i in range(3300):
    s[i] = f(i)
print(s[3027]-s[3023])