file24 = open('24var05.txt').readline()
mx = 0
A = 0
for i in range(len(file24)):
    if file24[i] == 'A':
        A = 1
        h = 0
        for j in range(i+1, len(file24)):
            if file24[j] == 'A':
                A += 1
            else: h += 1
            if A > 3:
                mx = max(mx, h+A-1)
                break
print(mx)

