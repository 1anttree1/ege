from ipaddress import *
net = ip_network('140.19.96.0/255.255.248.0', False)
h = 0
for i in net:
    f = str(i)
    k = f.split('.')
    l = []
    for (j) in k:
        j = int(j)
        if bin(j)[2:].count('1') in l:
            continue
        else:
            l.append(bin(j)[2:].count('1'))
    if len(l) == 1:
        h += 1

print(h)