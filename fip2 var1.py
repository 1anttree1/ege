file = open('24.gel.txt').readline()
ch = [str(i) for i in range(10)]
sim = 'AEIQUY'
count = 0
maxc = 0

def ysl(i,b):
    i + 3
    if ((file[i] in ch) and ( file[i+1] in ch) and file[i+2] in sim):
        if int(file[i] + file[i+1])%2 != 0:
            b += 1
            return ysl(i,b)
    else:
        return b
for i in range(len(file)-2):
    if ((file[i] in ch) and (file[i+1] in ch)) and (file[i+2] in sim):
        if int(file[i] + file[i+1])%2 != 0:
            print(ysl(i, 0))
            count = 1 + ysl(i, 0)
    else:
        maxc = max(maxc, count)
        count = 0
print(maxc)
