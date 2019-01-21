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
for i in range(n,q+1):
    if isprime(i):
        c=c+1
print(c)
