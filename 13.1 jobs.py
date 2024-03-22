from itertools import *
def func(n):
    c = nc = 0
    if int(str(n)[0]) % 2 == 0:
        for i in range(0, len(str(n)), 2):
            if n[i] % 2 == 0:
                c += 1
        for i in range(1, len(str(n)), 2):
            if n[i] % 2 != 0:
                nc += 1
    else:
        for i in range(1, len(str(n)), 2):
            if n[i] % 2 == 0:
                c += 1
        for i in range(0, len(str(n)), 2):
            if n[i] % 2 != 0:
                nc += 1
    if c + nc == 11:
        return True
    else:
        return False

def cnt(n):
    l = str(n)
    f = True
    for i in l:
        if l.count(i) < 4:
            f = True
        else:
            f = False
            break
    return f

a = product('12345678', repeat = 11)
s = [int(i) for i in a if cnt(i) == True and func(i) == True]
print(len(s))
