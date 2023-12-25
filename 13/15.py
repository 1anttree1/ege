from ipaddress import *
net = ip_network('252.67.33.87/255.252.0.0', False)
count = 0
for i in net:
    k = bin(int(i))[2:]
    if 2*k[:-16].count('1') < k[-16:].count('1'):
        count += 1
print(count)