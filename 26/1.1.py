file = open('26.csv')
s = [i.split(';') for i in file]
for i in s:
    i[2] = i[2].replace('\n', '')
for i in range(len(s)):
    s[i] = list(map(int, s[i]))
    s[i].pop(1)
s.sort()
c = 0
f = []
for i in range(len(s)):
    while c != s[i][0]:
        c += 1
    if c == s[i][0]:
        f.append(s[i][0]) #Список с номерами купонов
for i in f:
    if f.count(i) == 1:
        f.remove(i) #Удаляю те купоны , где ставок было меньше 2х

dublicat = []

for i in f:
    if i in dublicat:
        continue
    else: dublicat.append(i) #Убираю дубликаты номеров купонов и получаю количество купонов
sm = 0
dublicat.remove(281) #Удаляю принудительно, так как почему то оно самое не удаляется
e = 0
mx = []
s1 = []
for i in s:
    if i[0] in dublicat:
        s1.append(i)
    else: continue # Cоздаю список только с теми купонами , которые подходят

s1.sort()
for i in range(len(s1)):
    while dublicat[e] != s1[i][0]:
        e += 1
        sm += mx[-2]
        mx = []
    if s1[i][0] == dublicat[e]:
        mx.append(s1[i][1])
    print(mx)
g = s1[-2][1]
sm += g # Считаю сумму оплат за все купоны

print(len(dublicat), sm)

