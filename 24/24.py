file24 = open('24_9850.txt').readline()
count = mx = 0
for i in range(len(file24)):
    if file24[i] not in 'LISENOK' == False:
        count += 1
    else:
        mx = max(mx, count)
        count = 0
print(mx)