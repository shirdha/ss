n,k=map(int,input().split())
a=[]
for i in range(k,0,-1):
    if n%i==0 and k%i==0:
        a.append(i)
print(max(a))
