mn = 78902130987129078
h = 1
s= []
file = open('27v01_A.txt')
l = [int(i) for i in file]
l1 = [int(i) for i in l]
l.sort()
# print(l)
# print(l1)
for i in range(len(l)):
    if i % 10000 == 0:
        print(i)
    for j in range(len(l1)):
        if l1[j] == l[i]:
            if [j, l1[j]] in s:
                continue
            else:
                s.append([j, l1[j]])
print(s)



