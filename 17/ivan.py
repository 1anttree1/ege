with open("17.txt") as f:
    data = []
    for i in range(10):
        print(f.readline())
    for i in f:
        data = [int(i) for i in f]
print(data)