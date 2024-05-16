file = [int(i) for i in open('17-378.txt')]
mx1 = h = 0
mx = 652378490
for i in file:
    if i%1001 == 0:
        mx1 = max(mx1, abs(i))
print(mx1)
for i in range(len(file)-1):
    if ( len(str(abs(file[i]))) == 3 or len(str(abs(file[i+1]))) == 3 ) and (file[i]+file[i+1] > mx1):
        h += 1
        mx = min(mx, int(file[i])+int(file[i+1]))
print(h, mx)