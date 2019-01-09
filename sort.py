n=int(input(""))
c=0
a=list(map(int,input().split()))
s=[]
s=sorted(a)
for i in range(0,len(s)):
    if(c==0):
        print(s[i],end="")
        c=c+1
    else:
        print("",s[i],end="")
