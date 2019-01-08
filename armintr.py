def isprime(n):
    a=n
    s=0
    while(n>0):
       r=n%10
       s=s+r*r*r
       n=n//10
    if(a==s):
       return True
    else:
       return False
   
    
n,q=map(int,input().split())
c=0
for i in range(n+1,q):
    if isprime(i):
        if(c==0):
            print(i,end="")
            c=c+1
        else:
            print("",i,end="")

