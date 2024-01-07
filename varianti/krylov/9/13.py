from ipaddress import *
for i in range(1, 9):
    a = int(('1'*i + '0'*(8-i)), 2)
    net = ip_network(f'252.63.194.3/255.255.{a}.0', False)
    for x in net:
        p = bin(int(x))[2:]
        if (p[:-16].count('1') >= p[-16:].count('1')) == False:
            break
    else:
        print(a)
