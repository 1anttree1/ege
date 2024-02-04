
def f(n) :
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n>2:
        return s[n-1] + n*s[n-2]

s = [0]*1900
for i in range(1900):
    s[i] = f(i)

print(s[1890]//s[1885])