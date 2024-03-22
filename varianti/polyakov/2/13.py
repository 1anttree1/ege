from ipaddress import *
net = ip_network('216.130.64.0/255.255.192.0', False)
h = 0
for i in net:
    for j in str(i).split('.'):
        if int(j) %2 == 1:
            break
    else:
        h += 1
print(h)