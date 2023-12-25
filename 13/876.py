from ipaddress import *
for mask in range(32):
    net = ip_network(f'244.55.148.100/{mask}', False)
    if str(net.network_address) == '240.0.0.0' :
        print(IPv4Address(int('1' * mask + '0' * (32-mask), 2)))