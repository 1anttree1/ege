from ipaddress import *
for a in range(0, 256):
    net = ip_network(f'159.242.{a}.223/255.255.254.0', False)
    for i in net:
        nt = bin(int(i))[2:]
        if (nt[:-16].count('0') < nt[-16:].count('0')):
            print(a)