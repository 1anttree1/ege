for k in [x * 0.25 for x in range(-1000, 1000)]:
    p = k in [1, 12]
    q = k in [12, 13, 14, 15, 16]
    a = 0
    f = ((not a) <= ((not p) and (not q)))
    if f != 1:
        print(k)