file = open('27-v1a.txt')
s = []
l = [int(i) for i in file]
l1 =[int(i) for i in l]
l.sort(reverse=1)
for i in range(len(l)):
    for j in range(len(l1)):
        if l1[j] == l[i]:
            if [j, l1[j]] in s:
                continue
            else:
                s.append([j, l1[j]])
print(s)
