s1,s2=map(str,input().split())
c=0
if len(s2)<=len(s1):
    for i in s2:
        if i in s1:
            c=c+1
    if c==len(s2):
        print("yes")
    else:
        print("no")

else:
    print("no")
