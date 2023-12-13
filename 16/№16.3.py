import sys
sys.setrecursionlimit(10000)
def f1(n):
    if n > 2024:
        return n
    if n <= 2024:
        return n*f1(n+1)
print(f1(2022)/f1(2024), '____')



def f(n):
    if n > 2024:
        return n
    if n <= 2024:
        return n * s[n+1]
s = [1]*20233
for i in range(2026,1, -1):
    s[i] = f(i)
print(s[2022]/s[2024])
