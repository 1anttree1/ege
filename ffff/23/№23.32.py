def l(n,s):
    if n == s:
        return 1
    if n > s or n == 14:
        return 0
    if n < s:
        return l(n+1,s) + l(n+2, s)
print(l(2, 9) * l(9, 18))