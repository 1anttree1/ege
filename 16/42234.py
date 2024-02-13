import sys
sys.setrecursionlimit(100000)
def f(n):
    if n <= 1:
        return 0
    if n > 1 and n % 6 == 0:
        return n + f(n//6-2)
    if n > 1 and n % 6 != 0:
        return n + f(n+6)
# s = [0]*10000000
# for i in range(10000000):
#   s[i] = f(i)
# print(s[4242])
print(f(4242))