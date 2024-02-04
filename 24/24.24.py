file24 = open('24_12254.txt').readline()
h = mx = 1
for i in range(1, len(file24)):
    if file24[i-1] + file24[i] in ('RS', 'SQ', 'QR'):
        h += 1
        mx = max(mx, h)
    else:
        h = 1
print(mx)