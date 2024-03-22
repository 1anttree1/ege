from ipaddress import *
h =0
net = ip_network('117.32.0.0/255.224.0.0', False)
for i in net:
    f = str(i).split('.')
    l = [x for x in f if f.count(x) == 2]
    if len(l) == 2:
        h += 1
print(h)