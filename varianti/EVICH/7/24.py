file = open('24.txt').readline()
s = file.split(' ')
mx = 0
for i in s:
    mx = max(mx, len(i))
print(mx)