l=int(input())
n=list(map(int,input().split()))
d={}
r=[]
for i in n:
    c=n.count(i)
    d.update({i:c})
    r.append(d[i])


for x,y in d.items():
    if y==1:
        print(x)
