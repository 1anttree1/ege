from itertools import *
a = [''.join(i) for i in product('вася', repeat=5) if i.count("а")>0]
print(len(a))