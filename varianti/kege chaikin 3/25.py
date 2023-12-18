from fnmatch import *
for i in range(0, 10**8):
    if (i+1) % 2024 == 0:
        if fnmatch(str(i), '13*7?5'):
            # if (i+1)%2024 == 0:
            print(i, (i+1) // 2024)