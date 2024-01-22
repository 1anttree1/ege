from ipaddress import *
for i in range(1, 32):
    net = ip_network(f'244.55.138.100/{i}', False)
    if str(net.network_address) == '240.0.0.0':
        print(net)

#/цифра это количество едениц