a = 49**10 + 7**30 - 49
h = 0
while a > 0:
    if a%7 ==6:
        h +=1
    a //= 7
print(h)