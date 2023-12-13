file24 = open('24.txt').readline()
c = 0
a = 0
b = 0
mx = -1
for i in range(len(file24) -2):
    if (file24[i] == file24[i+1]):
        if file24[i+2] == "C":
            c += 1
        elif file24[i+2] == 'B':
            b += 1
        elif file24[i+2] == 'A':
            a += 1
mx = max(a,b,c)

print(mx, a, b, c)

