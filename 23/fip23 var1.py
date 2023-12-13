def k(n,s):
    if n == s:
        return 1
    if n > s or n == 11 or n == 17:
        return 0
    return k(n+1,s) + k(n+4, s) + k(n*2, s)
print(k(3, 24))