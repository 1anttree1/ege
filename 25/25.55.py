#27851
for i in range(210235,210300):
    s=0
    for d in range(2,int(i**0.5)):
        if i%d==0:
            s+=2
            if s>4:
                break
    if i**0.5%1==0:
        s+=1
    if s==4:
        for d in range(2, int(i ** 0.5)):
            if i%d==0:
                print(d,i/d)

