from fnmatch import *
for i in range(149, 10**8+1, 149):
    if fnmatch(str(i), '11*223'):
        print(i, i//149)