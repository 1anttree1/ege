for n in range(1, 255):
    l = bin(n)[2:]
    s = l[::-1]
    while s[0] == "0":
        s = s[1:]
    i = int(s, 2)
    if i == 13:
        print(n)
