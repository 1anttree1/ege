for i in range(10000, 100000):
    if (i%3 == 0) and (sum(map(int, (list(str(i))))) == int(str(i)[0]) * int(str(i)[1]) * int(str(i)[2]) * int(str(i)[3]) * int(str(i)[4])):
        print(i)