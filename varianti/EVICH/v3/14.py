s = '0123456789abc'
for i in s:
    f = int(f'186{i}4', 13) + int(f'5{i}716', 13)
    if f % 11 == 0:
        print(f//11)