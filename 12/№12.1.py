h = 0
k = 9
i = 0
a = '21'
while i != 34:
    a = '21'+ a
    while '21' in a:
        if '21' in a:
            a = a.replace('21', '5')
            k -= 1
            h += 1
    for l in a:
        i = i + int(l) + k

if i == 34:
    print(i, h)