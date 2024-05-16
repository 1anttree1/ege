file = [int(i) for i in open('17-377.txt')]
mx1 = mx = h =0
for i in file:
    if i%17 == 0:
        mx1 = max(mx1, i)

for i in range(len(file)-1):
    if file[i]+file[i+1] > mx1:
        h += 1
        mx = max(mx, file[i]+file[i+1])
print(h,mx)

