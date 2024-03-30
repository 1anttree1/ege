file24 = open('24.1.txt').readline()
h = 0
k = 0
mx = -1
print(len(file24))
for i in range(len(file24)):
    if file24[i] == 'Y':
        h = 1
        k = 1
        for j in range(i+1, len(file24)):
            if file24[j] == 'Y':
                h += 1
                k += 1
            else:
                h += 1
            if k>150:
                mx = max(mx, h) - 1
                break
print(mx)
