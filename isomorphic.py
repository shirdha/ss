s,r=map(str,input().split())
a=[]
b=[]
c=0
if len(s)==len(r):
    for i in s:
        u=s.count(i)
        a.append(u)
    for j in r:
        v=r.count(j)
        b.append(v)
    for m in range(len(a)):
        for n in range(len(b)):
            if m==n:
                if a[m]==b[n]:
                    c=c+1
    if(c==len(a)):
        print("yes")
    else:
        print("no")
else:
    print("no")
