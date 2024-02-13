file = open('24.txt').readline()
h = count = 0
mx = 0
for i in range(len(file)-1):
    if i% 10000 == 0:
        print(i)
    if file[i] == 'A':
        h = 0
        count = 0
        for j in range(i+1, len(file)):
            if file[j] == 'A':
                count += 1
                h += 1
                
            else: h += 1

            if count > 1:
                mx = max(mx,h) - 1
                break
print(mx)
