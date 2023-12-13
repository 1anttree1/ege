def l(n,s):
    if n == s:
        return 1
    if n > s or n == 10:
        return 0
    return l(n+1,s)+ l(n*2,s)

def d(n,s):
    if n == s:
        return 1
    if n > s or n == 9:
        return 0
    return d(n+1,s)+ d(n*2,s)
print(d(1,10)*d(10,20)+l(1,9)*l(9,20))