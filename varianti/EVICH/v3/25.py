from fnmatch import *
for i in range(163, 10**9+1, 163):
    if fnmatch(str(i), '3261??64*'):
        print(i, i//163)