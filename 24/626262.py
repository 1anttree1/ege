file = open('huibobra.txt').readline()
mx = 0

for i in range(len(file)):
    ab = []
    h = 0
    if file[i] in 'AB':
        ab.append(file[i])
        for j in range(i+1, len(file)):
            if file[j] in 'AB':
                ab.append(file[j])
            else:
                h += 1
            if ab.count('A') > 2 or ab.count('B') > 2:
                mx = max(mx, h+ab.count('B')+2)
                break

print(mx)