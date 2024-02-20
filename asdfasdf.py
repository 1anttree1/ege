# for i in range(1000, 10000):
#     s = []
#     i = str(i)
#     p = 0
#     for j in str(i):
#         p += i.count(j)
#     if p == 4:
#         for j in str(i):
#             s.append(j)
#         s.sort()
#         if len(s) > 0:
#             print(s)
#             sm = int(s[0]) + int(s[-1])
#             pr = int(s[1]) * int(s[2])
#             if sm<pr:
#                 f = str(sm)+str(pr)
#             else: f = str(pr) + str(sm)
#             if int(f) > 85:
#                 print(i)
#                 break


from itertools import *
a = product('гипербола', repeat = 6)
# s = [''.join(i) for i in a]
# gl = "иеоа"
sgl = "гпрбл"
h = 0
for i in s:
    if i[0] in sgl and i[-1] in sgl:
        for j in range(1, len(i)-1):
            if i[j] in gl and i[j-1] in sgl and i[j+1] in sgl:
                break
        else:
            h += 1
print(h)

# for i in range(1234567891011122, 9999999999999999+1):
#     r = str(i)[::-1]
#     sm1 = sm2 = sm = 0
#     for j in range(0, len(r), 2):
#         sm1 += int(r[j])
#     for j in range(1, len(r), 2):
#         f = str(int(r[j])*2)
#         if len(f) >1:
#             for k in f:
#                 sm2 += int(k)
#         else:
#             sm2 += int(f)
#     sm = sm1+sm2
#     if sm%10 == 0:
#         print(i)
#         break

# mx = 0
# for i in range(100, 1000):
#     f = str(i)
#     st = []
#     l = permutations(f, r = 2)
#     s = [''.join(j) for j in l]
#     h = 0
#     for j in s:
#         if j not in st and j[0] != '0':
#             st.append(j)
#         else:
#             continue
#     for j in st:
#         for k in range(2, int(int(j)**0.5)+1):
#             if int(j)%k == 0:
#                 break
#         else:
#             h += 1
#     mx = max(mx, h)

from itertools import *
# s = [''.join(i) for i in permutations('хочунабюджет', r = 12)]
# print(s)
a = permutations('хочунабюджет', r = 12)
s = []
for i in a:
    s.append(''.join(i))
    print()
print(s)