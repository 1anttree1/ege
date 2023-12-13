def perevod(n, s):
    string = ""
    while n != 0:
        string += str(n % s)
        n //= s
    return string[::-1]
k = 3*216**4 + 2*36**6 - 648
k = perevod(k, 6)
print(k.count('5'))