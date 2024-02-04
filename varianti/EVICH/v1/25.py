from fnmatch import *
for i in range(8161, 10**10+1, 8161):
    if fnmatch(str(i), '716??3*41'):
        print(i, i//8161)