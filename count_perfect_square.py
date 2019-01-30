l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    for j in range(1,i):
        if pow(j,2)==i:
            c=c+1
print(c)
