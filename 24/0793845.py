file = open('24-280.txt').readline()
s = []
mx = 0
for i in range(len(file)):
    s.append(file[i])
    for j in range(i+1, len(file)):
        if file[j] in s:
            mx = max(mx, len(s))
            s = []
            break
        else:
            s.append(file[j])
            mx = max(mx, len(s))
print(mx)