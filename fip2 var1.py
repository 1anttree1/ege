from itertools import *
a = product('0123456789abcde', repeat = 5)
s = [list(i) for i in a]
p = 0
h = 0
for i in s:
    for j in range(len(i)):
        i[j] = i[j].replace('a', '10')
        i[j] = i[j].replace('b', '11')
        i[j] = i[j].replace('c', '12')
        i[j] = i[j].replace('d', '13')
        i[j] = i[j].replace('e', '14')
        i[j] = i[j].replace('f', '15')



for i in s:
    p = 0
    if i[0] != '0':
        if int(i[0]) % 2 == 0:
            for j in range(len(i), 1):
                print(i[j])
                if int(i[j]) % 2 == 0:
                    p += 1
            for j in range(len(i)+1, 1):
                print(i[j])
                if int(i[j]) % 3 == 0:
                    p += 1
        if int(i[0]) % 3 == 0:
            for j in range(len(i), 1):
                print(i[j])
                if int(i[j]) % 3 == 0:
                    p += 1
            for j in range(len(i)+1, 1):
                print(i[j])
                if int(i[j]) % 2 == 0:
                    p += 1
        if p == 5:
            h += 1
print(h)