s = []
for i in range(100,1000):
    i = str(i)
    s.append(list(i))
h = k = 101
for i in range(len(s)):
    h += 1
    k = 101
    for j in range(len(s)):
        k += 1
        # print(h,k)
        sot = int(s[i][0]) + int(s[j][0])
        des = int(s[i][1]) + int(s[j][1])
        ed = int(s[i][2]) + int(s[j][2])
        controlsum = str(ed)+str(sot)+str(des)
        print(s[i], s[j], controlsum, controlsum[1:4])
        # if controlsum[1:4] == '002' or controlsum == '002':
        #     print(s[i], s[i+1])
        # print(str(s[i]) , str(s[j]))
