n=int(input())
k=list(map(int,input().split()))
s=sorted(k)
c=0
for i in range(len(k)):
    for j in range(len(s)):
        if i==j:
            if k[i]==s[j]:
                c=c+1
        
if c==len(k):
    print("yes")
else:
    print("no")
