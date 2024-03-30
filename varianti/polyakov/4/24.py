from itertools import *
file = open('24-212.txt').readline().replace('AB', '*').replace('AC', '*').replace('AD', '*').replace('OB', '*').replace('OC', '*').replace('OD', '*')
gl = 'AO'
sgl = 'BCD'
h = mx = 0
a = [''.join(i) for i in permutations('AOBCD', r=2) if i[0] in gl and i[1] in sgl]
for i in range(len(file)):
    if file[i] == '*':
        h += 1
        for j in range(i+1, len(file)):
            if file[j] == '*':
                h += 1
            else:
                mx = max(mx, h)
                h = 0
                break
print(mx, h)