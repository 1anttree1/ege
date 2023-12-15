for n in range(3, 1000):
    a = '2' + '5'*n
    while '25' in a or '355' in a or '555' in a:
        if '25' in a:
            a = a.replace('25', '32')
        if '355' in a:
            a = a.replace('355', '25')
        if '555' in a:
            a = a.replace('555', '2')





