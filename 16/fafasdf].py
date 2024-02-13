def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n * (n-1) + s[n-1] + s[n-2]
s = [0]*19999
for i in range(1, 10000):
    s[i] = f(i)
print(s[2024] - s[2022] - 2 * s[2021] - s[2020])