file24 = open('24_demka.txt').readline()
h = 0
mx = -1
k = 0
for i in range(len(file24)):
    if (file24[i] == 'X' and h%3 == 0) or (file24[i] == 'Y' and h%3 == 1) or (file24[i] == 'Z' and h%3 == 2):
        h += 1
    else:
        mx = max(mx, h)
        h = 0

print(mx)

