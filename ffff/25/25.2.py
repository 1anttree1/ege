from fnmatch import *
for i in range(0,10**10+1,2024):
    if fnmatch(str(i),'3?2258*4'):
        print(i)
