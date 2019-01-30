n=int(input())
val=1
while(val<=n):
    if n%val==0:
        if n%2!=0:
            print(format(val),end=" ") 
    val=val+1
