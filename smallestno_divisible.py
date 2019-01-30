n,k=map(int,input().split())
a=n*k
for i in range(1,a+1):
    if i%n==0 and i%k==0:
        print(i)
        break
    
