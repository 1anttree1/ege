from ipaddress import *
net = ip_network('202.75.38.160/255.255.255.240', False)
for i in net:
    f = bin(int(i))[2:]
    if '111' in f:
        print(f)