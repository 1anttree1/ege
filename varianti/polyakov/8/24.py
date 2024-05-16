file = open('24-1.txt').readline()
mx = h = c = 0

for i in range(len(file)-1):
    for j in range(i+1, len(file)):
        if file[j] == "A" or file[j] == "X" or file[j] == "B":
            c += 1
        if c >5 :
            mx = max(mx, h)
            h =0
            c = 0
            break
        else:
            h += 1
print(mx)