a=open("24_12254.txt").readline()
count=1
p=0
for i in range(len(a)-1):
    if a[i]=="R" and a[i+1]=='S':
        k=1
    elif a[i]=="S" and a[i+1]=="Q":
        k=1
    elif a[i]=="Q" and a[i+1]=="R":
        k=1
    else:
        k=0
    if k==1:
        count+=1
        # print(a[i],a[i+1])
    if k!=1:
        p=max(p,count)
        count=1
print(p)