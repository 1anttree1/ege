def perevod(n, s):
    st = ''
    while n > 0:
        st += str(n%s)
        n //= s
    return st[::-1]
print(bin(100)[2:], perevod(100, 2))