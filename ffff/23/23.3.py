def l(n,s):
    if n == s:
        return 1
    if n > s or n == 15:
        return 0
    return l(n+1,s) + l(n+2, s)
print(l(3,9) * l(9,20))