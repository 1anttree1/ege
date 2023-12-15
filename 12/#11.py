a =  '1' + '8'* 80
while('18' in a) or ('288' in a) or ('3888' in a):
    if '18' in a:
        a = a.replace('18', "2", 1)
    elif '288' in a:
        a = a.replace('288', "2", 1)
    else:
        a = a.replace('3888', "1", 1)
print(a)