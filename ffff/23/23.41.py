def l(n,s):
    if n == s:
        return 1
    if n > s:
        return 0
    return l(n+1,s) + l(n+2,s) + l(n+n-1, s)
print(l(2, 9))