file = open('24.txt').readline()
h = 1
mx = 0
for i in range(len(file)-1):
    if file[i] == file[i+1]:
        h += 1
    else:
        mx = max(mx, h)
        h = 1
print(mx)