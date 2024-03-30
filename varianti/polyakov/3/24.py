file = open('24-263.txt').readline()
h = 0
mx = 0
cy = 0
for i in range(len(file)-1):
    if file[i] == 'Y':
        cy = 1
        for j in range(i+1, len(file)):
            if file[j] == 'Y':
                cy += 1
            else: h += 1
            if cy == 151:
                mx = max(mx, h + cy-1)
                cy = 0
                h = 0
                break
    else: h += 1
print(mx)