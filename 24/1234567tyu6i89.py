file = open('24-33333333.txt').readline().replace('X', 'Z').replace('V', 'Z').split('Z')
mx = 0
for i in file:
    if i.count('A') <= 8 and i.count('E') <= 8 and i.count('I') <= 8 and i.count('O') <= 8 and i.count('U') <= 8 and i.count('Y') <= 8:
        mx = max(mx, len(i))
print(mx)