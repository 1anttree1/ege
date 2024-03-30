from ipaddress import *
net = ip_network('139.75.100.0/255.255.252.0', False)
a = [str(2**i - 1) for i in range(1, 9)]
h = 0
for i in net:
    f = str(i).split('.')
    print(type(f[-1]))
    if f[-1] in a:
        h += 1
print(h)