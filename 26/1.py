file = open('26.csv')
s = [i.split(';') for i in file]
for i in s:
    i[2] = i[2].replace('\n', '')
for i in range(len(s)):
    s[i] = list(map(int, s[i]))
    s[i].pop(1)
s.sort()
x=0
count=0
mx=[]
col=0
sm=0
for i in range(len(s)-1):
    x=s[i+1][0]
    mx.append(s[i][1])
    if x==s[i][0]:
        count+=1
    elif (count+1)<2:
        count=0
        print(s[i],s[i+1])
    else:
        col+=1
        sm+=sorted(mx)[-2]
        mx=[]
        count=0
print(col,sm)