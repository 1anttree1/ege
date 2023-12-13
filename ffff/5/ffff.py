for i in range(0, 256):
    n = bin(i)[2:]
    n = ('0' * (8 - len(n))) + n
    n = n.replace("0", "-")
    n = n.replace("1", "0")
    n = n.replace("-", "1")
    n = int(n, 2)
    raz = n - i
    if raz == 111:
        print(i)



