a,b=map(int,input().split())
d=list(map(int,input().split()))
c=0
for i in d:
    if i==b:
        print("yes")
        break
else:
    print("no")
