file17 = open('17_9872.txt')
a = []
def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result
mx = 0
for i in file17:
    a.append(int(i))
for i in range(len(a)):
    s = convert_to(int(a[i]), 13)
    # if len(s) > 2:
    #     print(s, i)
    #     break
    if len(s) >1:
        if s[-2] == '12':
            mx = max(mx, a[i])
print(mx)
for i in range(len(a)-2):
    h = 0
    if len(str(i)) == 3 and len(str(i+1)) == 3 and len(str(i+2)) == 2:
        h += 1
    if len(str(i)) == 2 and len(str(i+1)) == 3 and len(str(i+2)) == 3:
        h += 1
    if len(str(i)) == 3 and len(str(i+1)) == 2 and len(str(i+2)) == 3:
        h += 1
