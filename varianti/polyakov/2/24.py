file = open('24-264.txt').readline()
six = 'ABCDEF0123456789'
h = mx = 0
for i in range(len(file)-1):
    if file[i] in six:
        h+= 1
        for j in range(i+1, len(file)):
            if file[j] in six:
                h += 1
            else:
                mx = max(mx, h)
                h = 0
                break

print(mx)

