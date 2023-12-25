from ipaddress import *
for mask in range(32):
    net = ip_network(f"117.191.88.37/{mask}", False)
    if str(net.network_address) == '117.191.80.0':
        print(IPv4Address(int('1'*mask + '0'* (32-mask), 2)))