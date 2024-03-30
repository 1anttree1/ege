file = open('15.txt').readline()
s = ''
h = 0

for i in range(len(file)-1):
    if file[i] == 'A':
        s += file[i]
        for j in range(i+1, len(file)):
            s += file[j]
            print(s)
            if (s.count('A') > 1) or (len(s) > 15) or (s.count('B') > 1):
                s = ''
                break
            if s.count('B') == 1 and s[-1] == 'B' and s.count('F') > 0 and len(s) <= 15:
                print(s)
                h += 1
                s = ''
                break
print(h)