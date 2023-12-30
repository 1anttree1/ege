from ipaddress import *
net = ip_network('252.67.33.87/255.252.0.0', False)
h = 0
for i in net:
    p = bin(int(i))[2:]
    if p[-16:].count('1') > 2*p[:-16].count('1'):
        h += 1
print(h)