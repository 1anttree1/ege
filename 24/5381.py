from itertools import *
c = product('ABCDEFU', repeat = 3)
sgl = 'BCDF'
gl = 'AEU'
h = mx = 2
s = 0

cmb = [''.join(i) for i in c if (i[0] in sgl) and (i[1] in gl) and (i[2] in sgl)]

file = open('24_5381.txt').readline()

for i in range(len(file)-2):
    if file[i] + file[i+1] + file[i+2] in cmb:
        h += 1
        s += 1
        for j in range(i+1, len(file)-2):
            if file[j] + file[j + 1] + file[j + 2] in cmb:
                h += 3
                s += 1
            else:
                h += 1

            if s == 2:
                mx = max(mx, h)
                h = 2
                s = 0
                break
print(mx)
