file24 = open('24_demo (2).txt').readline()
h = 1
mx = -1
file24 = str(file24)
for i in range(len(file24)-1):
    if file24[i] + file24[i+1] == 'XX':
        h += 1
        mx = max(mx, h)
    else:
        h = 1

print(mx)
    