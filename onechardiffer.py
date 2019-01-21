s,r=map(str,input().split())
c=0
for m in range(len(s)):
    for n in range(len(r)):
        if m==n:
            if s[m]!=r[n]:
                c=c+1
if(c==1):
    print("yes")
else:
    print("no")
    
