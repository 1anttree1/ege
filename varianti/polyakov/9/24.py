file = open('24-1 (1).txt').readline()
h = mx = 0
for i in range(len(file)-1):
    a =0
    for j in range(i+1, len(file)):
        if file[j] == 'A':
            a += 1
        else:
            h += 1
        if a > 5:
            mx = max(mx, h+5)
            h = 0
            break
print(mx)