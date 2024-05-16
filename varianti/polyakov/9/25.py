from fnmatch import *
for i in range(2023, 10**9+1, 2023):
    if fnmatch(str(i), '20*23'):
        if (sum(list(map(int, str(i))))%7 == 0) and (sum(list(map(int, str(i))))<20):
            print(i, i/2023)