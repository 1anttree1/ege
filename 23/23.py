def l(n,s):
    if n == s:
        return 1
    if n > s :
        return 0
    if n < s :
        return l(n+2, s) + l(n*5, s)
print(l(2, 50))