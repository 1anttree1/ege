file = open('24-208.txt').readline().replace('2022', '*')
h = 0
mx = 0
c = 0
for i in range(len(file)-1):
    h += 1
    if file[i] == '*':
        c += 1
        for j in range(i+1, (len(file))):
            if file[j] == '*':
                c += 1
            else:
                h += 1
            if c == 5:
                mx = max(h+(c-1)*4, mx)
                c = 0
                h = 0
                break

print(mx)