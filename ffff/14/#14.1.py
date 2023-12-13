a = 9**18 +  3**54 - 9
h = ''

while a>0:
    h += str(a%3)
    a //= 3
h = h[:]

