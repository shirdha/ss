a,b=map(int,input().split())
n=list(map(int,input().split())) #list
c=0
for i in range(0,b):
    t=n[-1]
    del(n[-1])
    n.insert(0,t)
for i in range(len(n)):
    if(c==0):
        print(n[i],end="")
        c=c+1
    else:
        print("",n[i],end="")
