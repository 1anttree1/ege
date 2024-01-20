from ipaddress import *
for a in range(0, 256):
    net = ip_network(f'127.254.{a}.10/255.255.224.0', False)
    for i in net:
        ff = bin(int(i))[2:]
        if (ff[:-16].count('1') >= ff[-16:].count('1')) == False:
            break
    else:
        print(a)
        