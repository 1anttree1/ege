a = 7*5**1984 - 6 * 25**777 + 5*125**333 - 4
h = 0
def perevod(n, s):
    string = ""
    while n != 0:
        string += str(n % s)
        n //= s
    return string[::-1]

print(sum(list(map(int, perevod(a, 5)))))