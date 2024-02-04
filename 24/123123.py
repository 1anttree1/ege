file = open('24_9552.txt').readline()
file = file.replace('PC', '@')
file = file.replace('CSGO', '*')
h = 0
mx = 0
for i in range(len(file)):
    if file[i] == "@":
        h += 2
    elif file[i] == "*":
        h += 4
    else:
        mx = max(mx, h)
        h = 0
print(mx)