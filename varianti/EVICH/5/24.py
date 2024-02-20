file = open('24.txt').readline().replace('AD', '*')
s = []
for i in range(1, len(file)):
    if file[i] == '*':
        if file[i-1] == '*':
            s.append('D')
        else: s.append(file[i-1])

print(s.count('A'), s.count('B'), s.count('C'), s.count('D'))