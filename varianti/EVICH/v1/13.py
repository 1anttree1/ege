from ipaddress import *
for i in range(32):
    net = ip_network(f'185.49.83.72/{i}', False)
    if str(net.network_address) == '185.49.80.0':
        print(IPv4Address(int('1'*i + '0'* (32-i), 2)))