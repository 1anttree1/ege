file = open('24-275.txt').readline()
mx = h = 0
for i in range(len(file)-2):
    if file[i] + file[i+1] + file[i+2] == 'XYZ':
        continue
    if file[i] == 'X' and file[i+1] != 'Y':
