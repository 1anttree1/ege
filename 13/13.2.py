from ipaddress import *
net = ip_network("142.108.56.118/255.255.255.240", False)
count = 0
for i in net:
    p = bin(int(i))[2:]
    if p[:-16].count('1') < p[-16:].count('1'):
        count += 1
print(count)