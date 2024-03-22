
def perevod(n, s):
    string = ""
    while n != 0:
        string += str(n % s)
        n //= s
    return string[::-1]
print(perevod(210, 5))



# def perevod1(n, s):
#     l=[]
#     while n != 0:
#         if n % s==10:
#             l.append('a')
#         elif n%s==11:
#             l.append('b')
#         elif n%s==12:
#             l.append('c')
#         else:
#             l.append(str(n % s))
#         n //= s
#     return ''.join(l[::-1])
# for n in range(1,1001):
#     r=perevod1(n,12)
#     if n%12==0:
#         r+=r[-2:]
#     else:
#         r+=perevod(n%12*9,12)
#     if int(r,12)>300:
#         print(int(r,12))
#         break

