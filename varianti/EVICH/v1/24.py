file = open('24.txt').readline()
h = mx = 1
for i in range(len(file)-1):
    if ((file[i] in "ABCD") and (file[i+1] in "ABCD")) and( file[i]+file[i+1])!="CC" :

        h += 1
    else:
        mx = max(mx,h)
        h = 1

print(mx)