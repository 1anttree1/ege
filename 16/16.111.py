# import sys
# sys.setrecursionlimit(10000)
# def f(n):
#     if n < 11:
#         return n
#     if n >= 11:
#         return n +f(n-1)
# print(f(2024)-f(2021))

def f(n):
    if n < 11:
        return n
    if n >= 11:
        return n + s[n-1]
s = [1]*2025
for i in range(1,2025):
    s[i] = f(i)
print(s[2024] - s[2021])
