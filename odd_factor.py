n=int(input())
val=1
c=0
while(val<=n):
    if n%val==0:
        if val%2==1:
            if c==0:
                print(val,end="")
                c+=1
            else:
                print("",val,end="")
    val=val+1
