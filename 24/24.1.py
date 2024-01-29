file = open('24_9169.txt').readline()
file = file.replace('FAT', '@') #замена
file = file.replace('BAD', '@') #замена
h = count = 0
mn = 10000

for i in range(len(file)):
    if file[i] == "@":
        count += 1
        h += 1
        for j in range(i+1, len(file)):
            if file[j] == "@":
                count += 1
                h += 1
            else:
                h += 1
            if count == 3:
                mn = min(mn, h + 6)
                h = count = 0
                break
print(mn)
