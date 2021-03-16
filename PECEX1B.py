t=int(input())

for _ in range(t):
    n=int(input())
    a,b,c,d=-1,-1,-1,-1

    for i in range(2,int(n**0.5)+1):
        b2=(n-i**2)**0.5
        if b2%1==0 and b2>0:
            if b2>=i:
                a=i
                b=int(b2)
                break
            else:
                a=int(b2)
                b=i
                break
    flag=False
    if b!=-1:
        for i in range(b+1,int(n**0.5)+1):
            b2=(n-i**2)**0.5
            if b2%1==0 and b2>0:
                d=i
                c=int(b2)
                flag=True
                break
    if not flag:
        a=-1
        b=-1
    print(a,b,c,d)
