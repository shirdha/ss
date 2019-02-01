a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in range(0,a-b):
    if d==0:
        print(c[i],end="")
        d=d+1
    else:
        print("",c[i],end="")
