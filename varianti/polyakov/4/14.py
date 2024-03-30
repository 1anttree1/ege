import sys
sys.set_int_max_str_digits(100000)
h = 0
n = 7*512**3200 + 5*256**3100 - 5*64**3000 - 4 * 8 **2900 - 1542
while n != 0:
    if n%64 == 0:
        h += 1
    n //= 64
print(h)