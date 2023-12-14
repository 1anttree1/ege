def ff(n,s):
    if n == s:
        return 1
    if n>s or n == 23:
        return 0
    return ff(n+2, s) + ff(n*3, s) + ff(n*5, s)
print(ff(1,13)* ff(13,75))
for i in range(1,101):
    print("")