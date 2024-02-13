for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            s = '0' + '2'*i + '4'*j + '6'*k
            while '02' in s or '04' in s or '06' in s:
                if '02' in s:
                    s = s.replace('02', '6404', 1)
                if '04' in s:
                    s = s.replace('04', '2206', 1)
                if '06' in s:
                    s = s.replace('06', '440', 1)

            if s.count('2') == 30 and s.count('4') == 54 and s.count('6') == 10:
                print(k)
