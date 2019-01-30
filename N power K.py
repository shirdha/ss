n,k=map(int,input().split())
c=0
for i in range(1,n+1):
    if k**i==n:
        c=c+1
if c==1:
    print("yes")
else:
    print("no")
