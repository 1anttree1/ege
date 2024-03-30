file = [int(i) for i in open('17-379.txt')]
mx = h = mx1 = 0
for i in file:
    if str(i)[-2:] == '15':
        mx = max(mx, i)

for i in range(len(file) - 2):
    if ((((len(str(file[i])) == 4) + (len(str(file[i + 1])) == 4) + (len(str(file[i + 2])) == 4)) == 1) and (
            file[i] + file[i + 1] + file[i + 2]) >= mx):
        h += 1
        mx1 = max(mx1, file[i] + file[i + 1] + file[i + 2])
print(h, mx1)
