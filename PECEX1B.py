t=int(input())

for _ in range(t):
    n=int(input())
    a,b,c,d=-1,-1,-1,-1

    for i in range(2,int(n**0.5)+1):
        b2=(n-i**2)**0.5
        if b2%1==0 and b2>0:
            a=i
            b=int(b2)
            if a>b:
                a,b=b,a
            break
    flag=False
    if b!=-1:
        for i in range(min(b+1,a+1),int(n**0.5)+1):
            b2=(n-i**2)**0.5
            if b2%1==0 and b2>0 and int(b2)!=a and int(b2)!=b:
                d=i
                c=int(b2)
                if c>d:
                    c,d=d,c
                flag=True
                break
    if not flag:
        a=-1
        b=-1
    if b>d:
        a,b,c,d=c,d,a,b
    print(a,b,c,d)