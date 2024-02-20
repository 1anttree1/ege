file = open('24-222222222.txt').readline().replace('X','Y').split('Y')
mx = 0
for i in file:
    if i.count('S') <= 10 and i.count('U') <= 10 and i.count('N') <= 10:
        mx = max(mx, len(i))
print(mx)