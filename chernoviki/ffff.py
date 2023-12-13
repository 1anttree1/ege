# mx = 0
# for n in range(1, 10000):
#     r = bin(n)[2:]
#     l = list(r)
#     for i in range(0, len(l), 2):
#         l[i] = '*'
#     l = ''.join(l)
#     if l.count('0') > l.count('1'):
#         r = r.replace('1', '*')
#         r = r.replace('0', '1')
#         r = r.replace('*', '0')
#     else:
#         print(r)
#         r = list(r)
#         for i in range(1, len(r), 2):
#             r[i] = '1'
#         r = ''.join(r)
#         print(r)
#     r = int(r, 2)
#     if r <= 1337:
#         mx = max(mx, r)
#
#     if r == 1337:
#         print(n)
#         break



# for n in range(1000):
#     sm = 0
#     k = 0
#     st = '!' + '2'*19 + '0' * 15 + '1'*n
#     while '!1' in st or '!2' in st or '!0' in st:
#         if '!1' in st:
#             st = st.replace('!1', '2!', 1)
#         if '!2' in st:
#             st = st.replace('!2', "30!", 1)
#         if '!0' in st:
#             st = st.replace('!0', '1!', 1)
#     st = st.replace('0', '5', 1)
#     st = st.replace('!', '', 1)
#     for i in st:
#         sm = sm + int(i)
#     for i in range(1,15):
#         for j in range(1,15):
#             if sm == i**2 + j**2:
#                 print(n)


def f(n):
    if n<3:
        return n
    if n>2:
        return (2*n-1)*(s[n-1]+s[n-2])
s = [1]*100
for i in range(1, 71):
    s[i] = f(i)

print(s[69]%(10**9+7))



# def f(n):
#     if n == 0:
#         return 0
#     if (n**0.5)%1 == 0:
#         return s[n-1] - n
#     else: return s[n-1] + n
# s = [0]*77
# for i in range(0, 77):
#     s[i] = f(i)
# print(s[25])



