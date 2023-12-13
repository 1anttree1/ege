def perevod(n, s):
     string = ""
     while n != 0:
         string += str(n % s)
         n //= s
     return string[::-1]

for n in range(1, 1000):
    sum1 = 0
    mx = 0
    r = perevod(n, 8)
    for i in str(n):
        sum1 +=int(i)
    if sum1%2 ==0:
        r += str(n%3)
    if sum1%2 ==1:
        for i in str(r):
            mx = max(mx,int(i))
        r = str(mx) + r
    if int(r, 8) > 127:
        print(n)