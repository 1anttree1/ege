from ipaddress import *
net = ip_network('202.75.38.176/255.255.255.240', False)
h = 0
for i in net:
    r = bin(int(i))
    if ('000' in r) or ('111' in r):
        continue
    else: h += 1
print(h)