a,b,c=map(str,input().split())
d=int(c)
e=0
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            if a[i]!=b[j]:
                e+=1
if e==d:
    print("yes")
else:
    print("no")
