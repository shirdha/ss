def prime(n):
    c=0 #initializing the count as 0
    for i in range(2,n-1):
        if(n%i==0):
            c=c+1
    if(c==0):
        return True
    else:
        return False

n=int(input(""))
val=2
d=0
while(val<=n):
    if n%val==0:
        if prime(val):
            if d==0:
                print(format(val),end="") 
                d=d+1
            else:
                print("",format(val),end="")
    val=val+1
