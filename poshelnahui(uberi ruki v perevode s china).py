def f(n):
    if n >= 2024:
        return 1
    if n < 2024:
        return f(n+2) + f(n+4)
l = set()
for i in range(2023, -1, -1):
    if i%10 == 0:
        print(i)
    l.add(f(i))
print(len(l))