from ipaddress import *
for mask in range(32):
    net = ip_network(f'109.171.211.176/{mask}', False)
    print(IPv4Address(int('1' * mask + '0' * (32 - mask), 2)))