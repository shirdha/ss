def isprime(n):
    c=0
    for i in range(2,n-1):
      if(n%i==0):
          c=c+1
    if(c==0):
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
