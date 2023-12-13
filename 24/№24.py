file24 = open('24_demo(1).txt').readline()
mx = -1
h = 1
for i in range(len(file24)-1):
    if file24[i] != file24[i+1]:
        h += 1
        mx = max(mx, h)
    else:
        h = 1
print(mx)