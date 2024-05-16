file = open('open')
mx = h = 0
c = '123'
b = 'RSY'
for i in range(len(file)):
    for j in range(len(i+1, file)):
        if (file[j] in c and file[j+1] in b) or (file[j] in b and file[j+1] in c):
            h += 1
        else:
            mx = max(mx, h)
            h =0
            break