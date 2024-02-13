from ipaddress import *
for mask in range(32):
    net = ip_network(f'172.49.54.172/{mask}', False)
    if str(net.network_address) == '172.49.48.0':
        print(int('11111000', 2))
