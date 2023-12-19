import math
for x in range(1, 100000):
    if (math.sqrt(14 + math.sqrt(1 + math.sqrt(11 - math.sqrt(x))))) == 4:
        print(x)