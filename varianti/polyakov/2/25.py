from fnmatch import *
for i in range(1923, 10**8+1, 1923):
    if fnmatch(str(i),'1*2??76'):
        print(i, i//1923)
        